from __future__ import print_function, division, absolute_import

import logging


def set_logging(level):
    format = ("%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s")
    logging.basicConfig(format=format, level=logging.WARNING)

    logger = logging.getLogger("k2d")
    logger.setLevel(level)
