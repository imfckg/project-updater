from sys import platform

import pytest

from project_scanner.main import GitProjectScanner


class TestGitProjectScanner:
    @pytest.fixture
    def git_scanner(self, temporary_git_project):
        return GitProjectScanner(temporary_git_project)

    def test_scan_with_git_directory(self, git_scanner):
        # Arrange
        expected_result = [str(git_scanner.path)]
        # Act
        result = list(git_scanner)
        # Assert
        assert result == expected_result

    def test_scan_without_git_directory(self, tmp_path):
        # Arrange
        scanner = GitProjectScanner(tmp_path)
        # Act
        result = list(scanner)
        # Assert
        assert result == []

    def test_scan_at_depth_0(self, git_scanner):
        # Arrange
        git_scanner.depth = 0
        # Act
        result = list(git_scanner)
        # Assert
        assert result == []

    def test_scan_multiple_directories(self, tmp_path):
        # Arrange
        match platform:
            case 'win32':
                expected_result = [
                    str(tmp_path),
                    str(tmp_path / 'dir1'),
                    str(tmp_path / 'dir2'),
                    str(tmp_path / 'dir3'),
                ]
            case 'linux' | 'darwin':
                expected_result = [
                    str(tmp_path),
                    str(tmp_path / 'dir2'),
                    str(tmp_path / 'dir3'),
                    str(tmp_path / 'dir1'),
                ]
            case _:
                raise ValueError(f'Unsupported platform: {platform}')

        dir1 = tmp_path / 'dir1' / '.git'
        dir2 = tmp_path / 'dir2' / '.git'
        dir3 = tmp_path / 'dir3' / '.git'
        git_dir = tmp_path / '.git'
        git_dir.mkdir(parents=True)
        dir1.mkdir(parents=True)
        dir2.mkdir(parents=True)
        dir3.mkdir(parents=True)
        scanner = GitProjectScanner(tmp_path)
        # Act
        result = list(scanner)
        # Assert
        assert result == expected_result

    def test_iter_method(self, git_scanner):
        # Arrange
        expected_result = [str(git_scanner.path)]
        # Act
        result = list(iter(git_scanner))
        # Assert
        assert result == expected_result

    def test_next_method(self, git_scanner):
        # Arrange
        expected_result = [str(git_scanner.path)]
        # Act
        result = [next(git_scanner) for _ in range(len(expected_result))]
        # Assert
        assert result == expected_result
