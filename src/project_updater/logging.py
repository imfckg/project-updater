import logging


def setup_debug_loggers(*args: str) -> None:
    formatter = logging.Formatter(
        fmt="[%(asctime)s][%(levelname)s][%(module)s] ==> %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    for name in args:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
