import logging
import sys


def setup_logging(debug: bool) -> None:
    """Setup logging configuration."""
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)

    if debug:
        logger.setLevel(logging.DEBUG)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
