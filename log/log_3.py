import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

logging.debug("디버깅 메시지입니다.")
logging.info("정보성 메시지입니다.")
logging.warning("경고 메시지입니다.")
logging.error("에러 메시지입니다.")
logging.critical("치명적 에러 메시지입니다.")