import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] %(filename)s:%(lineno)d [%(levelname)s] %(message)s')
file_handler = logging.FileHandler('./log.txt', encoding='utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("디버깅 메시지입니다.")
logger.info("정보성 메시지입니다.")
logger.warning("경고 메시지입니다.")
logger.error("에러 메시지입니다.")
logger.critical("치명적 에러 메시지입니다.")