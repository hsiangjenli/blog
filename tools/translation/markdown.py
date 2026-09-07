"""Markdown and front-matter primitives that preserve post bodies."""

import re

import yaml


FRONT_MATTER_BOUNDARY = re.compile(r"^---\s*$")


def split_front_matter(markdown: str) -> tuple[dict, str]:
    """Split a Markdown document into parsed YAML metadata and body text."""
    lines = markdown.splitlines()
    if not lines or not FRONT_MATTER_BOUNDARY.match(lines[0]):
        return {}, markdown
    for index in range(1, len(lines)):
        if FRONT_MATTER_BOUNDARY.match(lines[index]):
            return yaml.safe_load("\n".join(lines[1:index])) or {}, "\n".join(lines[index + 1 :]).lstrip("\n")
    return {}, markdown


def join_front_matter(metadata: dict, body: str) -> str:
    """Write YAML metadata without changing the Markdown body structure."""
    document = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{document}\n---\n\n{body.rstrip()}\n"


def normalize_language(language: object) -> str:
    """Normalize accepted Chinese locale spellings to the site locale."""
    value = str(language or "").strip().lower()
    if value in {"zh", "zh-tw", "zh_tw", "zh-hant", "zh-hant-tw"}:
        return "zh-TW"
    return "en" if value else ""
