#!/usr/bin/env python3
"""Check that each published post is available in English and Traditional Chinese."""

from pathlib import Path
import sys

from translation.validation import missing_translations


def main() -> None:
    """Print missing post counterparts and exit nonzero when the site is incomplete."""
    missing = missing_translations(Path("source/_posts"))
    if not missing:
        print("All posts have both en and zh-TW translations.")
        return
    print("Missing translations for the following slugs:")
    for slug, languages in sorted(missing.items()):
        print(f"- {slug}: missing {', '.join(sorted(languages))}")
    sys.exit(2)


if __name__ == "__main__":
    main()
