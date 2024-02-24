from .log import logger


def run(*args, **kwargs):
    logger.debug('CLI args: %s, kwargs: %s', args, kwargs)
