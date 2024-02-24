import os
import sys
from typing import Final

from project_updater import cli

from . import __version__
from .logging import setup_debug_loggers

WELCOME_MESSAGE: Final[str] = f'PROJECT UPDATER v{__version__}'


def main():
    print(WELCOME_MESSAGE)
    if os.getenv('DEBUG'):
        setup_debug_loggers(cli.log.LOGGER_NAME)
    sys.exit(cli.commands.run())


if __name__ == '__main__':
    main()
