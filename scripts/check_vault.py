#!/usr/bin/env python3
"""Read-only structural checks for a BrainDock vault (not a privacy audit)."""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

REQUIRED = ('README.md', 'Start Here.md', 'AGENTS.md', 'VAULT-SPEC.md',
            'SECURITY.md', 'Projects/00 Projects.md')
SKIP = {'.git', '.obsidian', '.trash', '.venv', '__pycache__', '.pytest_cache'}
MACHINE_PATH = re.compile(r'/(?:Users|home)/[^\s/]+|[A-Za-z]:[\\/]Users[\\/]|file://', re.I)
MARKDOWN_LINK = re.compile(r'!?\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)\)')
WIKILINK = re.compile(r'\[\[([^\]\n]+)\]\]')
PLACEHOLDER = re.compile(r'\{\{[^{}\n]+\}\}')


def prose(text: str) -> str:
    """Exclude fenced and inline examples from link/placeholder checks."""
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.sub(r'(`+).*?\1', '', '\n'.join(lines))


def metadata_ok(text: str) -> bool:
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        return False
    fields = dict(re.findall(r'^([\w-]+):[ \t]*(.*)$', match.group(1), re.M))
    if any(not fields.get(key, '').strip() for key in ('type', 'tags', 'updated')):
        return False
    try:
        value = fields['updated'].strip('\'" ')
        return bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', value)) and bool(date.fromisoformat(value))
    except ValueError:
        return False


def check(root: Path) -> tuple[list[str], int]:
    if root.is_symlink():
        return ['vault root: symlink is unsupported; skipped'], 0
    root = root.resolve()
    issues: list[str] = []
    if not root.is_dir():
        return ['required vault directory does not exist'], 0
    files: dict[str, Path] = {}
    for folder, dirs, names in os.walk(root, followlinks=False):
        base = Path(folder)
        if base != root and '.git' in dirs + names:
            issues.append(f'{base.relative_to(root)}: nested repository is unsupported; skipped')
            dirs[:] = []
            continue
        kept = []
        for name in sorted(dirs):
            path = base / name
            if path.is_symlink():
                issues.append(f'{path.relative_to(root)}: symlink is unsupported; skipped')
            elif name not in SKIP:
                kept.append(name)
        dirs[:] = kept
        for name in sorted(names):
            path = base / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                issues.append(f'{relative}: symlink is unsupported; skipped')
            elif name not in SKIP:
                files[relative] = path
    for name in REQUIRED:
        if name not in files:
            issues.append(f'{name}: required record missing')
    by_filename: dict[str, list[str]] = defaultdict(list)
    for name, path in files.items():
        by_filename[path.name].append(name)
    notes = {name: path for name, path in files.items() if path.suffix.lower() == '.md'}
    stems: dict[str, list[str]] = defaultdict(list)
    for name, path in notes.items():
        stems[path.stem.casefold()].append(name)
    for matches in stems.values():
        if len(matches) > 1:
            issues.append('duplicate Markdown filename: ' + ', '.join(matches))

    def resolve_link(source: str, raw: str, wiki: bool) -> None:
        target = raw.split('|', 1)[0] if wiki else raw.strip('<>')
        try:
            parsed = urlsplit(target)
        except ValueError:
            issues.append(f'{source}: broken link (invalid URL)')
            return
        if parsed.scheme or parsed.netloc:
            return
        target = unquote(parsed.path)
        if not target:
            return
        base = root / Path(source).parent
        candidate = (base / target).resolve()
        if not candidate.is_relative_to(root):
            issues.append(f'{source}: link outside vault: {raw}')
            return
        candidates = [candidate.relative_to(root).as_posix()]
        if wiki:
            candidates.append(target.removeprefix('./'))
            candidates += [p + '.md' for p in candidates if not Path(p).suffix]
            if '/' not in target:
                matches = stems.get(Path(target).stem.casefold(), [])
                if len(matches) == 1:
                    candidates += matches
                candidates += by_filename.get(target, [])
        if not any(p in files for p in candidates):
            issues.append(f'{source}: broken link: {raw}')

    for name, path in notes.items():
        try:
            text = path.read_text(encoding='utf-8-sig')
        except (OSError, UnicodeError):
            issues.append(f'{name}: unreadable UTF-8 note')
            continue
        if not metadata_ok(text):
            issues.append(f'{name}: metadata needs non-empty type, tags, and ISO updated date')
        if MACHINE_PATH.search(text):
            issues.append(f'{name}: machine path found; use portable relative locations')
        content = prose(text)
        is_template = name.startswith('Templates/') and path.name != '00 Templates.md'
        if not is_template and PLACEHOLDER.search(content):
            issues.append(f'{name}: unresolved placeholder')
        if is_template:
            continue
        for raw in MARKDOWN_LINK.findall(content):
            resolve_link(name, raw, False)
        for raw in WIKILINK.findall(content):
            resolve_link(name, raw, True)
    return sorted(issues), len(notes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        issues, count = check(args.root)
    except OSError as error:
        print(f'ERROR: filesystem could not be inspected ({type(error).__name__})')
        return 1
    for issue in issues:
        print('ERROR:', issue)
    print(f'{count} Markdown notes checked; {len(issues)} structural issue(s).')
    print('This is not a privacy, evidence, or publication-safety audit.')
    return 1 if issues else 0


if __name__ == '__main__':
    raise SystemExit(main())
