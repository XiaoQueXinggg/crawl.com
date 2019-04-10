import logging
logging.basicConfig(level=logging.WARN)
logger=logging.getLogger(__name__)

logger.debug('there is a bug')
logger.critical('are you stupid')
logger.warning('stop do it')
logger.info('over')
