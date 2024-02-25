import subprocess
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temporary_git_project():
    temp_dir = tempfile.TemporaryDirectory()
    git_dir = Path(temp_dir.name) / '.git'
    git_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'init'], cwd=temp_dir.name, check=True)
    yield Path(temp_dir.name)
    temp_dir.cleanup()
