"""ログ用モジュール."""
import logging.config

from .settings import LOGGING_CONF


def get_my_logger(name):
    logging.config.dictConfig(LOGGING_CONF)
    return logging.getLogger(name)


logger = get_my_logger(__name__)


if __name__ == '__main__':
    """my_loggingを試しに使ってみる."""
    logger.debug('DEBUGレベルです')
    logger.info('INFOレベルです')
    logger.warning('WARNINGレベルです')
    logger.error('ERRORレベルです')
    logger.critical('CRITICALレベルです')
