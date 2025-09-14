#!/usr/bin/env python3
import re
from pathlib import Path
import yaml

FM_BOUND = re.compile(r'^---\s*$')

def split_front_matter(text: str):
    lines = text.splitlines(True)
    if not lines or not FM_BOUND.match(lines[0].rstrip('\n')):
        return {}, text
    for i in range(1, len(lines)):
        if FM_BOUND.match(lines[i].rstrip('\n')):
            fm = ''.join(lines[1:i])
            body = ''.join(lines[i+1:])
            data = yaml.safe_load(fm) or {}
            return data, body
    return {}, text

def join_front_matter(data: dict, body: str) -> str:
    fm = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm}\n---\n\n{body.lstrip()}"

def is_lang_suffix(stem: str) -> bool:
    low = stem.lower()
    return low.endswith('.en') or low.endswith('.zh-tw') or low.endswith('.zh_tw') or low.endswith('.zh')

def cleanup_body(body: str) -> str:
    lines = body.splitlines(True)
    # find first non-empty line
    j = 0
    while j < len(lines) and lines[j].strip() == '':
        j += 1
    if j >= len(lines):
        return body
    first = lines[j]
    if not first.lstrip().startswith('>'):
        return body
    # Only clean if AI notice
    plain = first.lstrip('> ').strip()
    if not (plain.startswith('註記：此頁為由 AI') or plain.startswith('Note: This page is an AI-generated')):
        return body
    # Collect initial quoted block
    i = j
    quoted = []
    while i < len(lines) and lines[i].lstrip().startswith('>'):
        quoted.append(lines[i])
        i += 1
    rest = ''.join(lines[i:])
    # Try to preserve a heading inside the quote
    heading = None
    for ql in quoted:
        m = re.match(r'^\s*>\s*(#\s+.*)$', ql)
        if m:
            heading = m.group(1).rstrip('\n')
            break
    new_body = ''
    if heading:
        new_body += heading + '\n\n'
    new_body += rest.lstrip('\n')
    return ''.join(lines[:j]) + new_body

def main():
    root = Path('source/_posts')
    changed = 0
    for p in root.glob('*.md'):
        stem = p.stem
        text = p.read_text(encoding='utf-8')
        fm, body = split_front_matter(text)
        orig_fm = dict(fm)
        orig_body = body
        # Remove AI-generated markers
        fm.pop('source_sha', None)
        fm.pop('origin_lang', None)
        fm.pop('translation_key', None)
        # Cleanup AI notice at top if present
        # Only try to clean notice on likely originals (no lang suffix)
        body = cleanup_body(body) if not is_lang_suffix(stem) else body
        if fm != orig_fm or body != orig_body:
            p.write_text(join_front_matter(fm, body), encoding='utf-8')
            changed += 1
            print(f"cleaned: {p}")
    print(f"Done. Files updated: {changed}")

if __name__ == '__main__':
    main()
