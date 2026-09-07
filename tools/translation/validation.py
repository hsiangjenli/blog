"""Validate that every published post has all requested language versions."""

from pathlib import Path
import re

from .markdown import normalize_language, split_front_matter


LANGUAGE_SUFFIX = re.compile(r"\.(en|zh-TW|zh_tw|zh)$", re.IGNORECASE)


def post_slug(metadata: dict, path: Path) -> str:
    """Use explicit slug first, then a filename with its locale suffix removed."""
    return str(metadata.get("slug") or LANGUAGE_SUFFIX.sub("", path.stem))


def missing_translations(posts_dir: Path, languages: set[str] | None = None) -> dict[str, set[str]]:
    """Report missing language variants, skipping drafts."""
    expected = languages or {"en", "zh-TW"}
    grouped: dict[str, set[str]] = {}
    for path in posts_dir.rglob("*.md"):
        metadata, _ = split_front_matter(path.read_text(encoding="utf-8"))
        if metadata.get("draft", False):
            continue
        language = normalize_language(metadata.get("lang") or metadata.get("language"))
        if not language:
            language = "zh-TW" if LANGUAGE_SUFFIX.search(path.stem) and ".en" not in path.stem else "en"
        grouped.setdefault(post_slug(metadata, path), set()).add(language)
    return {slug: expected - present for slug, present in grouped.items() if expected - present}
