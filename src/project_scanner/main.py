from pathlib import Path
import os
from typing import Iterator, Final


class GitProjectScanner:
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
            self.__search(self.path, self.current_depth)
        if self.iterator_position < len(self.found_directories):
            result = self.found_directories[self.iterator_position]
            self.iterator_position += 1
            return result
        else:
            raise StopIteration

    def __search(self, current_path: Path, current_depth: int):
        if current_depth > 0:
            for entry in os.listdir(current_path):
                entry_path = current_path / entry
                if entry_path.is_dir():
                    if entry == '.git':
                        self.found_directories.append(str(current_path))
                        break
                    else:
                        self.__search(entry_path, current_depth - 1)


def main():
    # Пример использования
    path_to_search = Path('/Users/im/GitHub/imfckg/')
    depth_to_search = 3

    git_scanner = GitProjectScanner(path_to_search, depth_to_search)
    print('Список папок с подпапкой .git:')
    for directory in git_scanner:
        print(directory)
