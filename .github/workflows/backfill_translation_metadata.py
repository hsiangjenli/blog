#!/usr/bin/env python3
"""Backfill multilingual Hexo post front-matter with permalink and translations metadata."""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Tuple

import yaml

FM_BOUNDARY = re.compile(r"^---\s*$")
DATE_PREFIX = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+)$", re.IGNORECASE)
LANG_SUFFIXES = {"en", "zh", "zh-tw", "zh_tw"}


def normalize_lang(lang: str) -> str:
    if not lang:
        return ""
    value = str(lang).strip().lower()
    if value in {"zh", "zh-tw", "zh_tw", "zh-hant", "zh-hant-tw"}:
        return "zh-TW"
    return "en"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def split_front_matter(markdown: str) -> Tuple[Dict, str]:
    lines = markdown.splitlines()
    if not lines or not FM_BOUNDARY.match(lines[0]):
        return {}, markdown
    for idx in range(1, len(lines)):
        if FM_BOUNDARY.match(lines[idx]):
            fm_block = "\n".join(lines[1:idx])
            body_block = "\n".join(lines[idx + 1 :])
            data = yaml.safe_load(fm_block) or {}
            return data, body_block.lstrip("\n")
    return {}, markdown


def join_front_matter(data: Dict, body: str) -> str:
    fm_text = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).strip()
    body = body.rstrip()
    return f"---\n{fm_text}\n---\n\n{body}\n"


def ensure_slug(raw: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", str(raw)).strip("-").lower()
    return cleaned or "post"


def infer_slug(data: Dict, path: Path) -> str:
    if data.get("slug"):
        return ensure_slug(data["slug"])
    if data.get("title"):
        return ensure_slug(data["title"])
    stem = path.stem
    if "." in stem:
        parts = stem.split(".")
        if parts[-1].lower() in LANG_SUFFIXES:
            stem = ".".join(parts[:-1])
    match = DATE_PREFIX.match(stem)
    if match:
        return ensure_slug(match.group("slug"))
    return ensure_slug(stem)


def detect_lang(path: Path, data: Dict, fallback: str) -> str:
    lang = data.get("lang") or data.get("language")
    normalized = normalize_lang(lang)
    if normalized:
        return normalized
    stem = path.stem.lower()
    if stem.endswith(tuple(f".{suffix}" for suffix in LANG_SUFFIXES)):
        suffix = stem.split(".")[-1]
        return normalize_lang(suffix)
    return fallback


def build_permalink(lang: str, slug: str, default_lang: str) -> str:
    lang = normalize_lang(lang) or lang
    if not slug:
        return ""
    if lang == default_lang:
        candidate = f"{slug}.{lang}"
    else:
        candidate = f"{lang}/{slug}"
    return candidate if candidate.endswith("/") else f"{candidate}/"


def format_translation_url(permalink: str) -> str:
    value = (permalink or "").strip()
    if not value:
        return ""
    if not value.startswith("/"):
        value = "/" + value
    if not value.endswith("/"):
        value += "/"
    return value


def load_posts(root: Path, default_lang: str) -> Dict[str, Dict[str, Dict]]:
    groups: Dict[str, Dict[str, Dict]] = defaultdict(dict)
    for path in sorted(root.rglob("*.md")):
        if path.is_dir():
            continue
        raw = read_text(path)
        fm, body = split_front_matter(raw)
        slug = infer_slug(fm, path)
        lang = detect_lang(path, fm, default_lang)
        groups[slug][lang] = {
            "path": path,
            "front_matter": fm,
            "body": body,
            "lang": lang,
            "slug": slug,
            "changed": False,
        }
    return groups


def sync_group(entries: Dict[str, Dict], slug: str, default_lang: str, dry_run: bool) -> int:
    changed_count = 0
    permalink_map: Dict[str, str] = {}

    for lang, entry in entries.items():
        fm = entry["front_matter"]
        if fm.get("slug") != slug:
            fm["slug"] = slug
            entry["changed"] = True
        if normalize_lang(fm.get("lang") or fm.get("language")) != lang:
            fm["lang"] = lang
            entry["changed"] = True
        permalink = fm.get("permalink")
        if not permalink:
            permalink = build_permalink(lang, slug, default_lang)
            if permalink:
                fm["permalink"] = permalink
                entry["changed"] = True
        else:
            permalink = permalink.strip()
            if permalink and not permalink.endswith("/"):
                fm["permalink"] = f"{permalink}/"
                permalink = fm["permalink"]
                entry["changed"] = True
        if permalink:
            permalink_map[lang] = format_translation_url(permalink)

    if len(permalink_map) > 1:
        ordered_langs = sorted(permalink_map.keys())
        for lang, entry in entries.items():
            fm = entry["front_matter"]
            desired = {other: permalink_map[other] for other in ordered_langs if other != lang}
            current = fm.get("translations") or {}
            if current != desired:
                if desired:
                    fm["translations"] = desired
                elif "translations" in fm:
                    fm.pop("translations")
                entry["changed"] = True
    else:
        for entry in entries.values():
            fm = entry["front_matter"]
            if "translations" in fm:
                fm.pop("translations")
                entry["changed"] = True

    for entry in entries.values():
        if entry["changed"] and not dry_run:
            content = join_front_matter(entry["front_matter"], entry["body"])
            write_text(entry["path"], content)
            changed_count += 1
        elif entry["changed"]:
            changed_count += 1
            print(f"[dry-run] {entry['path']}")
    return changed_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Fill missing multilingual metadata for Hexo posts.")
    parser.add_argument("--posts-dir", default="source/_posts", help="Directory containing Markdown posts.")
    parser.add_argument("--default-lang", default="en", help="Site default language.")
    parser.add_argument("--dry-run", action="store_true", help="Show files that would change without writing.")
    args = parser.parse_args()

    posts_root = Path(args.posts_dir).resolve()
    if not posts_root.exists():
        print(f"Error: {posts_root} does not exist", file=sys.stderr)
        sys.exit(1)

    default_lang = normalize_lang(args.default_lang) or "en"
    groups = load_posts(posts_root, default_lang)

    total_files = 0
    for slug, entries in groups.items():
        total_files += sync_group(entries, slug, default_lang, args.dry_run)

    if args.dry_run:
        print(f"Dry run complete. {total_files} file(s) would be updated.")
    else:
        print(f"Done. {total_files} file(s) updated.")


if __name__ == "__main__":
    main()