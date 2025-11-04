import argparse
import os
import re
import sys
import hashlib
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import yaml

try:
    from openai import OpenAI
except ImportError:
    print("Missing openai. pip install openai pyyaml", file=sys.stderr)
    sys.exit(2)

FM_BOUND = re.compile(r'^---\s*$')
DATE_PREFIX = re.compile(r'^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+)$', re.IGNORECASE)

def read_text(p: Path) -> str:
    return p.read_text(encoding='utf-8')

def write_text(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding='utf-8')

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def split_front_matter(md: str):
    lines = md.splitlines()
    if not lines or not FM_BOUND.match(lines[0]):
        return {}, md
    # find closing ---
    for i in range(1, len(lines)):
        if FM_BOUND.match(lines[i]):
            fm = "\n".join(lines[1:i])
            body = "\n".join(lines[i+1:])
            data = yaml.safe_load(fm) or {}
            return data, body.lstrip("\n")
    return {}, md

def join_front_matter(data: dict, body: str) -> str:
    fm = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm}\n---\n\n{body.rstrip()}\n"

def normalize_lang(lang: str) -> str:
    if not lang:
        return ""
    return ("zh-TW" if str(lang).lower() in ["zh", "zh-tw", "zh_tw", "zh-hant", "zh-hant-tw"] else "en")

def infer_key(data: dict, path: Path) -> str:
    # Prefer explicit translation_key, then slug, then filename slug, then kebab-case title
    if data.get("translation_key"):
        return str(data["translation_key"])
    if data.get("slug"):
        return str(data["slug"])
    stem = path.stem
    # strip language suffix like .zh-TW/.en
    if '.' in stem:
        parts = stem.split('.')
        if parts[-1].lower() in ['en', 'zh-tw', 'zh_tw', 'zh']:
            stem = ".".join(parts[:-1])
    m = DATE_PREFIX.match(stem)
    base = m.group('slug') if m else stem
    title = data.get("title")
    if title:
        base = re.sub(r'[^a-zA-Z0-9]+', '-', str(title)).strip('-').lower() or base
    return base

def parse_date_from_filename(path: Path, fallback: str) -> str:
    m = DATE_PREFIX.match(path.stem.split('.')[0])
    if m:
        return m.group('date')
    # fallback front-matter date (yyyy-mm-dd) or today
    try:
        return datetime.fromisoformat(str(fallback)).date().isoformat()
    except Exception:
        return datetime.utcnow().date().isoformat()

def detect_lang_from_path(path: Path, fm_lang: str) -> str:
    # Trust front-matter first
    if fm_lang:
        return normalize_lang(fm_lang)
    # else infer from suffix
    stem = path.stem
    if stem.endswith('.zh-TW') or stem.endswith('.zh_tw') or stem.endswith('.zh'):
        return "zh-TW"
    if stem.endswith('.en'):
        return "en"
    return ""

def target_filename(src_path: Path, target_lang: str, key_slug: str) -> Path:
    # keep same date and base slug, append .<lang> if needed
    m = DATE_PREFIX.match(src_path.stem.split('.')[0])
    date_part = m.group('date') if m else None
    base = key_slug
    if date_part:
        fname = f"{date_part}-{base}.{target_lang}.md"
    else:
        fname = f"{base}.{target_lang}.md"
    return src_path.with_name(fname)

def ensure_slug(key: str) -> str:
    s = re.sub(r'[^a-zA-Z0-9]+', '-', str(key)).strip('-').lower()
    return s or str(key)

def build_permalink(lang: str, slug: str, default_lang: str) -> str:
    if not slug:
        return ''
    normalized_lang = normalize_lang(lang) or lang
    if normalized_lang == default_lang:
        path = f"{slug}.{normalized_lang}"
    else:
        path = f"{normalized_lang}/{slug}"
    return path if path.endswith('/') else path + '/'

def format_translation_url(path: str) -> str:
    if not path:
        return ''
    value = '/' + path.lstrip('/')
    return value if value.endswith('/') else value + '/'

def translate_text(client: OpenAI, model: str, text: str, src_lang: str, dst_lang: str, title: str):
    sys_prompt = (
        "You are a professional bilingual translator. "
        "Translate Markdown from {src} to {dst}. "
        "Preserve Markdown structure, code fences, links, and inline formatting. "
        "Do not hallucinate or add content. Keep list/heading levels. "
        "If the content contains any names, places, or technical terms, keep them unchanged. "
        "Return a compact JSON with keys: title, body. "
        "If the content contains comments in the format <!-- Terms: [Original Term] = [Translated Term] -->, use those mappings to translate the specified terms."
    ).format(src=("Traditional Chinese" if src_lang=="zh-TW" else "English"),
             dst=("Traditional Chinese" if dst_lang=="zh-TW" else "English"))

    user_prompt = f"""Source title:
{title or ''}

Source markdown body:
{text}
"""

    resp = client.chat.completions.create(
        model=model,
        response_format={"type":"json_object"},
        messages=[
            {"role":"system","content": sys_prompt},
            {"role":"user","content": user_prompt}
        ],
    )
    content = resp.choices[0].message.content
    try:
        data = yaml.safe_load(content)  # JSON is YAML-compatible
        return str(data.get("title","")), str(data.get("body",""))
    except Exception:
        # Fallback: treat whole as body
        return title, content

def prepend_notice(body: str, src_lang: str, dst_lang: str, model: str) -> str:
    # Add a locale-specific note that this article is AI translated.
    if dst_lang == "zh-TW":
        note = f"註記：此頁為由 AI（{model}）自動翻譯自英文原文，可能含有少量不準確之處。"
    else:
        # default to English
        source_label = "Traditional Chinese" if src_lang == "zh-TW" else "English"
        note = f"Note: This page is an AI-generated ({model}) translation from {source_label} and may contain minor inaccuracies."
    # Use a single-line blockquote, then leave a plain blank line to terminate the quote.
    return f"> {note}\n\n{body.lstrip()}"

def load_posts(root: Path):
    posts = []
    for p in root.rglob("*.md"):
        if p.is_dir():
            continue
        md = read_text(p)
        fm, body = split_front_matter(md)
        lang = normalize_lang(fm.get("lang") or "")
        lang_from_path = detect_lang_from_path(p, fm.get("lang"))
        if not lang:
            lang = lang_from_path or "en"
        key = infer_key(fm, p)
        slug = ensure_slug(fm.get("slug") or key)
        date = parse_date_from_filename(p, str(fm.get("date","")))
        posts.append({
            "path": p,
            "fm": fm,
            "body": body,
            "lang": lang,
            "key": key,
            "slug": slug,
            "date": date,
            "content_sha": sha256(body),
        })
    return posts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src-root", required=True)
    ap.add_argument("--default-lang", default="en")
    ap.add_argument("--other-lang", default="zh-TW")
    ap.add_argument("--changed-file-list", default="")
    ap.add_argument("--scan-all", action="store_true")
    ap.add_argument("--model", default="gpt-4o-mini")
    args = ap.parse_args()

    root = Path(args.src_root).resolve()
    if not root.exists():
        print(f"Missing {root}", file=sys.stderr)
        sys.exit(1)

    api_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    if not api_key:
        print("Missing OPENAI_API_KEY. Please set it in GitHub Actions secrets or environment.", file=sys.stderr)
        sys.exit(2)
    base_url_raw = (os.environ.get("OPENAI_API_BASE") or "").strip()
    if not base_url_raw:
        base_url = "https://api.openai.com/v1"
    else:
        base_url = base_url_raw if base_url_raw.startswith("http://") or base_url_raw.startswith("https://") else ("https://" + base_url_raw)
    client = OpenAI(api_key=api_key, base_url=base_url)

    posts = load_posts(root)
    # index by (slug, lang)
    by_slug_lang = {}
    by_path = {}
    slug_index = defaultdict(dict)
    for it in posts:
        by_slug_lang[(it["slug"], it["lang"])] = it
        by_path[str(it["path"])] = it
        slug_index[it["slug"]][it["lang"]] = it

    # Determine work set
    changed = set()
    if args.changed_file_list and Path(args.changed_file_list).exists() and not args.scan_all:
        for line in read_text(Path(args.changed_file_list)).splitlines():
            pth = line.strip()
            if not pth:
                continue
            path = Path(pth).resolve()
            if str(path) in by_path:
                changed.add(by_path[str(path)]["path"])
    do_all = args.scan_all or not changed

    default_lang = normalize_lang(args.default_lang) or "en"
    other_lang = normalize_lang(args.other_lang) or "zh-TW"
    targets = {default_lang, other_lang}

    language_order = []
    for lang in [default_lang, other_lang]:
        if lang and lang not in language_order:
            language_order.append(lang)

    slugs_to_sync = set()

    def save_item(item, fm, body_override=None):
        body_value = body_override if body_override is not None else item["body"]
        write_text(item["path"], join_front_matter(fm, body_value))
        item["fm"] = fm
        if body_override is not None:
            item["body"] = body_override
            item["content_sha"] = sha256(body_override)

    def sync_slug(slug_value):
        entries = slug_index.get(slug_value)
        if not entries or len(entries) < 2:
            return

        for lang_key, item_obj in entries.items():
            fm_current = dict(item_obj["fm"])
            desired_permalink = build_permalink(lang_key, slug_value, default_lang)
            if desired_permalink and not fm_current.get("permalink"):
                fm_current["permalink"] = desired_permalink
            if fm_current != item_obj["fm"]:
                save_item(item_obj, fm_current)

        path_map = {}
        for lang_key, item_obj in entries.items():
            fm_current = item_obj["fm"]
            permalink_value = fm_current.get("permalink") or build_permalink(lang_key, slug_value, default_lang)
            if not permalink_value:
                continue
            path_map[lang_key] = format_translation_url(permalink_value)

        if not path_map:
            return

        for lang_key, item_obj in entries.items():
            fm_current = dict(item_obj["fm"])
            translations_map = {}

            for ordered_lang in language_order:
                if ordered_lang == lang_key:
                    continue
                url = path_map.get(ordered_lang)
                if url:
                    translations_map[ordered_lang] = url

            for other_lang_key in sorted(path_map.keys()):
                if other_lang_key == lang_key or other_lang_key in translations_map:
                    continue
                translations_map[other_lang_key] = path_map[other_lang_key]

            if translations_map:
                if fm_current.get("translations") != translations_map:
                    fm_current["translations"] = translations_map
            else:
                if "translations" in fm_current:
                    del fm_current["translations"]
                else:
                    continue

            if fm_current != item_obj["fm"]:
                save_item(item_obj, fm_current)

    updates = 0
    for it in posts:
        # skip drafts
        if it["fm"].get("draft", False):
            continue

        # If changed-only mode, process only sources that changed in this push
        if not do_all and it["path"] not in changed:
            continue

        # Only treat files WITHOUT 'source_sha' as human-authored sources.
        # Prevent "both directions" updates that could overwrite originals.
        if "source_sha" in it["fm"]:
            # This file is a generated translation; do not use it as a source to update others.
            continue

        slug = it["slug"]
        src_lang = it["lang"]

        # Backfill source front-matter with slug/lang if missing (do NOT enforce translation_key)
        src_fm_new = None
        if not it["fm"].get("slug"):
            src_fm_new = dict(it["fm"]) if src_fm_new is None else src_fm_new
            src_fm_new["slug"] = slug
        # Normalize lang field to canonical form
        if normalize_lang(it["fm"].get("lang") or "") != src_lang:
            src_fm_new = dict(it["fm"]) if src_fm_new is None else src_fm_new
            src_fm_new["lang"] = src_lang
        if src_fm_new is not None:
            save_item(it, src_fm_new)
        for dst_lang in targets - {src_lang}:
            counterpart = by_slug_lang.get((slug, dst_lang))
            source_body_sha = it["content_sha"]

            if counterpart is not None:
                slugs_to_sync.add(slug)

            # Case 1: counterpart missing -> create translation
            if counterpart is None:
                print(f"[create] {slug} {src_lang} -> {dst_lang}")
                title_src = str(it["fm"].get("title",""))
                title_dst, body_dst = translate_text(client, args.model, it["body"], src_lang, dst_lang, title_src)
                body_dst = prepend_notice(body_dst, src_lang, dst_lang, args.model)

                fm_new = dict(it["fm"])  # copy
                fm_new["title"] = title_dst or fm_new.get("title")
                fm_new["lang"] = dst_lang
                fm_new["slug"] = slug  # keep same slug across languages
                fm_new["date"] = it["fm"].get("date") or it["date"]
                fm_new["source_sha"] = source_body_sha
                fm_new["origin_lang"] = src_lang
                fm_new["permalink"] = build_permalink(dst_lang, slug, default_lang)
                fm_new.pop("translations", None)

                dst_path = target_filename(it["path"], dst_lang, slug)
                write_text(dst_path, join_front_matter(fm_new, body_dst))
                # update in-memory indices for subsequent loops
                new_item = {
                    "path": dst_path, "fm": fm_new, "body": body_dst, "lang": dst_lang,
                    "key": it["key"], "slug": slug, "date": fm_new["date"],
                    "content_sha": sha256(body_dst),
                }
                by_slug_lang[(slug, dst_lang)] = new_item
                by_path[str(dst_path)] = new_item
                slug_index[slug][dst_lang] = new_item
                slugs_to_sync.add(slug)
                updates += 1
                continue

            # Case 2: counterpart exists -> update only if source changed
            counterpart_fm = counterpart["fm"]
            cp_source_sha = str(counterpart_fm.get("source_sha") or "")
            if do_all:
                should_update = (cp_source_sha != source_body_sha)
            else:
                should_update = (cp_source_sha != source_body_sha) and (it["path"] in changed)

            if should_update:
                print(f"[update] {slug} {src_lang} -> {dst_lang}")
                title_src = str(it["fm"].get("title",""))
                title_dst, body_dst = translate_text(client, args.model, it["body"], src_lang, dst_lang, title_src)
                body_dst = prepend_notice(body_dst, src_lang, dst_lang, args.model)

                new_fm = dict(counterpart_fm)
                new_fm["title"] = title_dst or new_fm.get("title")
                new_fm["lang"] = dst_lang
                new_fm["slug"] = slug
                new_fm["date"] = counterpart_fm.get("date") or it["fm"].get("date") or it["date"]
                new_fm["source_sha"] = source_body_sha
                new_fm["origin_lang"] = src_lang
                if not new_fm.get("permalink"):
                    new_fm["permalink"] = build_permalink(dst_lang, slug, default_lang)
                new_fm.pop("translations", None)

                save_item(counterpart, new_fm, body_dst)
                slug_index[slug][dst_lang] = counterpart
                slugs_to_sync.add(slug)
                updates += 1

    if do_all:
        slugs_pending = {slug for slug, entries in slug_index.items() if len(entries) >= 2}
    else:
        slugs_pending = slugs_to_sync

    for slug_value in sorted(slugs_pending):
        sync_slug(slug_value)

    print(f"Done. Updated/created: {updates}")
    # exit 0 always; git diff step decides whether to commit

if __name__ == "__main__":
    main()
