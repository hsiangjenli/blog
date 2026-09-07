"""Metadata helpers shared by translation creation and synchronization."""


def permalink(language: str, slug: str, default_language: str) -> str:
    """Keep the established English root and Traditional Chinese URL layout."""
    path = slug if language == default_language else f"{language}/{slug}"
    return f"{path}/"


def translation_map(paths: dict[str, str], current_language: str) -> dict[str, str]:
    """Return the other locale URLs for one post's front matter."""
    return {language: f"/{path.lstrip('/')}" for language, path in paths.items() if language != current_language}
