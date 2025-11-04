#!/usr/bin/env python3
import sys
import re
from pathlib import Path
import yaml

FM_BOUND = re.compile(r'^---\s*$')
DATE_PREFIX = re.compile(r'^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+)$', re.IGNORECASE)


def read_text(p: Path) -> str:
    return p.read_text(encoding='utf-8')


def split_front_matter(md: str):
    lines = md.splitlines()
    if not lines or not FM_BOUND.match(lines[0]):
        return {}, md
    for i in range(1, len(lines)):
        if FM_BOUND.match(lines[i]):
            fm = "\n".join(lines[1:i])
            body = "\n".join(lines[i + 1:])
            data = yaml.safe_load(fm) or {}
            return data, body
    return {}, md


def normalize_lang(lang: str) -> str:
    if not lang:
        return ""
    s = str(lang).lower()
    if s in ["zh", "zh-tw", "zh_tw", "zh-hant", "zh-hant-tw"]:
        return "zh-TW"
    return "en"


def detect_lang_from_content(text: str) -> str:
    # Improved heuristic:
    # - Remove fenced code blocks, inline code, markdown links/images and URLs before counting
    # - Count CJK characters and ASCII letters, then decide based on ratio and minimum total
    import re

    # remove fenced code blocks ```...``` (multiline)
    text = re.sub(r'```[\s\S]*?```', ' ', text)
    # remove inline code `...`
    text = re.sub(r'`[^`]*`', ' ', text)
    # remove markdown links/images [alt](url) and ![alt](url)
    text = re.sub(r'!?\[[^\]]*\]\([^\)]*\)', ' ', text)
    # remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # remove URLs
    text = re.sub(r'https?://\S+', ' ', text)

    cjk = sum(1 for ch in text if (
        '\u4e00' <= ch <= '\u9fff' or  # CJK Unified Ideographs
        '\u3400' <= ch <= '\u4dbf' or  # CJK Ext A
        '\uf900' <= ch <= '\ufaff' or  # CJK Compatibility Ideographs
        '\u3000' <= ch <= '\u303f'     # CJK punctuation
    ))
    letters = sum(1 for ch in text if ('a' <= ch.lower() <= 'z'))

    total = cjk + letters
    # require a minimum amount of text to decide
    if total < 50:
        return ''

    # compute CJK ratio
    ratio = cjk / total if total > 0 else 0.0
    if ratio >= 0.6:
        return 'zh-TW'
    if ratio <= 0.4:
        return 'en'
    return ''


def detect_lang_from_path(path: Path, fm_lang: str) -> str:
    if fm_lang:
        return normalize_lang(fm_lang)
    stem = path.stem
    if stem.endswith('.zh-TW') or stem.endswith('.zh_tw') or stem.endswith('.zh'):
        return "zh-TW"
    if stem.endswith('.en'):
        return "en"
    return ""


def ensure_slug(base: str) -> str:
    s = re.sub(r'[^a-zA-Z0-9]+', '-', str(base)).strip('-').lower()
    return s or base


def infer_slug(data: dict, path: Path) -> str:
    # Prefer explicit slug, then filename slug, then kebab-case title
    if data.get("slug"):
        return ensure_slug(str(data["slug"]))
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
        base = ensure_slug(re.sub(r'[^a-zA-Z0-9]+', '-', str(title)).strip('-').lower()) or base
    return ensure_slug(base)


def main():
    root = Path('source/_posts').resolve()
    if not root.exists():
        print(f"No posts directory at {root}", file=sys.stderr)
        sys.exit(1)

    pairs = {}
    missing = {}

    for p in root.rglob('*.md'):
        if p.is_dir():
            continue
        raw = read_text(p)
        fm, body = split_front_matter(raw)
        if fm.get('draft', False):
            # Skip drafts from completeness requirement
            continue
        declared = normalize_lang(fm.get('lang') or '')
        path_lang = detect_lang_from_path(p, fm.get('lang'))
        content_lang = detect_lang_from_content(body)
        # Prefer declared/path if consistent, otherwise fall back to content detection
        candidates = [declared, path_lang, content_lang]
        lang = next((x for x in candidates if x), '') or 'en'
        slug = infer_slug(fm, p)
        entry = pairs.setdefault(slug, set())
        entry.add(lang)
        # Report suspicious mismatch between declared lang and content
        if declared and content_lang and declared != content_lang:
            print(f"WARN: Language mismatch in {p}: declared {declared}, content looks {content_lang}")

    for slug, langs in pairs.items():
        needed = {"en", "zh-TW"}
        missing_langs = sorted(list(needed - langs))
        if missing_langs:
            missing[slug] = missing_langs

    if missing:
        print("Missing translations for the following slugs:")
        for slug, langs in sorted(missing.items()):
            print(f"- {slug}: missing {', '.join(langs)}")
        print("\nPlease run the translation workflow or backfill to complete translations.")
        sys.exit(2)

    print("All posts have both en and zh-TW translations. ✅")


if __name__ == '__main__':
    main()
