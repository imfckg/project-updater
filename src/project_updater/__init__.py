import importlib.metadata
from pathlib import Path
from typing import Final

LIBRARY_NAME: Final[str] = 'project_updater'


def __get_package_version() -> str:
    """Find the version of this package."""
    __package_version = 'undefined'
    try:
        __package_version = importlib.metadata.version(LIBRARY_NAME)
    except importlib.metadata.PackageNotFoundError:
        import toml

        pyproject_toml_file = Path(__file__).parent.parent / 'pyproject.toml'
        if pyproject_toml_file.exists() and pyproject_toml_file.is_file():
            __package_version = toml.load(pyproject_toml_file)['tool']['poetry'][
                'version'
            ]
            __package_version = __package_version + '+'

    return __package_version


__all__: Final[list[str]] = []
__version__ = __get_package_version()
__author__ = 'Ivan Migunov <im@fckg.ru>'
__license__ = 'MIT'
