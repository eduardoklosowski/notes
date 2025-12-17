#!/usr/bin/env python3

import os
from pathlib import Path
from typing import Iterable

INDEX_FILENAME = 'README.md'


def sort_paths(files: Iterable[Path]) -> Iterable[Path]:
    yield from sorted(
        (
            f
            for f in files
            if f.is_dir() or (f.name.endswith('.md') and f.name != INDEX_FILENAME)
        ),
        key=lambda f: read_title(f).upper(),
    )


def read_title(file: Path) -> str:
    try:
        if file.is_dir():
            file /= INDEX_FILENAME
        with file.open() as fd:
            first_line = fd.readline()
    except Exception:
        first_line = ''

    if first_line.startswith('# '):
        return first_line.removeprefix('# ').strip()
    if file.name == INDEX_FILENAME:
        return file.parent.name
    return file.name.removesuffix('.md')


def print_page(page_path: Path) -> None:
    indent = '  ' * (len(page_path.parts) - 1)
    path = page_path
    if path.is_dir():
        path /= INDEX_FILENAME
    title = read_title(path)
    if path.exists():
        link = path.as_posix()
    else:
        link = ''
    print(f'{indent}- [{title}]({link})')
    if page_path.is_dir():
        for c in sort_paths(page_path.iterdir()):
            print_page(c)


def main(path: Path) -> None:
    os.chdir(path)

    root = Path('.')
    sections = sort_paths(f for f in root.iterdir() if f.is_dir())

    print('# Índice')
    print()
    print(f'[Notas]({INDEX_FILENAME})')
    for section in sections:
        print_page(section)


if __name__ == '__main__':
    import sys

    main(Path(sys.argv[0]).parent)
