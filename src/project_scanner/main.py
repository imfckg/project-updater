from pathlib import Path
import os
from typing import Iterator, Final


class GitProjectScanner:
    __slots__ = (
        'path',
        'depth',
        'current_depth',
        'found_directories',
        'iterator_position',
    )

    path: Path
    depth: int
    current_depth: int
    found_directories: list[str]
    iterator_position: int

    DEFAULT_DEPTH: Final[int] = 3

    def __init__(self, path: Path, depth: int = DEFAULT_DEPTH):
        self.path = path
        self.depth = depth
        self.current_depth = 0
        self.found_directories = []
        self.iterator_position = 0

    def __iter__(self) -> Iterator[str]:
        self.found_directories = []
        self.current_depth = self.depth
        self.iterator_position = 0
        return self

    def __next__(self) -> str:
        if not self.found_directories:
            self.scan(self.path, self.current_depth)
        if self.iterator_position < len(self.found_directories):
            result = self.found_directories[self.iterator_position]
            self.iterator_position += 1
            return result
        else:
            raise StopIteration

    def scan(self, current_path: Path, current_depth: int) -> list[str]:
        """
        Осуществляет поиск вложенных Git проектов в заданном каталоге.

        :param current_path: Путь к текущему каталогу
        :param current_depth: глубина поиска
        """
        if current_depth > 0:
            if '.git' in os.listdir(current_path):
                self.found_directories.append(str(current_path))
            for entry in os.listdir(current_path):
                entry_path = current_path / entry
                if entry_path.is_dir():
                    self.scan(entry_path, current_depth - 1)
        return self.found_directories


def main():
    for directory in GitProjectScanner(Path('/Users/im/GitHub/')):
        print(directory)


if __name__ == '__main__':
    for directory in GitProjectScanner(Path('/Users/im/GitHub/')):
        print(directory)
