from pathlib import Path
import os
from typing import Iterator
import argparse


class GitProjectScanner:
    DEFAULT_DEPTH: int = 3

    def __init__(self, path: Path, depth: int = DEFAULT_DEPTH):
        self.path = path
        self.depth = depth
        self.iterator = self.scan(self.path, self.depth)

    def __iter__(self) -> Iterator[str]:
        yield from self.scan(self.path, self.depth)

    def __next__(self):
        return next(self.iterator)

    def scan(self, current_path: Path, current_depth: int) -> Iterator[str]:
        """
        Осуществляет поиск вложенных Git проектов в заданном каталоге.

        :param current_path: Путь к текущему каталогу
        :param current_depth: глубина поиска
        """
        if current_depth > 0:
            if '.git' in os.listdir(current_path):
                yield str(current_path)
            for entry in os.listdir(current_path):
                entry_path = current_path / entry
                if entry_path.is_dir():
                    yield from self.scan(entry_path, current_depth - 1)


def main():
    parser = argparse.ArgumentParser(description='project-scanner')
    parser.add_argument('path', type=str, help='path to scan projects')

    args = parser.parse_args()
    for directory in GitProjectScanner(Path(args.path)):
        print(directory)


if __name__ == '__main__':
    main('.')
