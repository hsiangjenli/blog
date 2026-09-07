"""Pair translated posts by stable slug and language."""

from collections import defaultdict
from typing import Any


def group_by_slug(posts: list[dict[str, Any]]) -> dict[str, dict[str, dict[str, Any]]]:
    """Index posts by their common slug and language."""
    groups: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for post in posts:
        groups[post["slug"]][post["lang"]] = post
    return groups


def original_post(posts: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    """Choose the human-authored counterpart regardless of its language."""
    return next((post for post in posts.values() if "source_sha" not in post["fm"]), None)
