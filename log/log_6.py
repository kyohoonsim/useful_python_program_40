import coloredlogs, logging

def show_log():
    logging.debug("디버깅 메시지입니다.")
    logging.info("정보성 메시지입니다.")
    logging.warning("경고 메시지입니다.")
    logging.error("에러 메시지입니다.")
    logging.critical("치명적 에러 메시지입니다.")

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', 
fmt='''%(asctime)s %(created)f %(filename)s %(funcName)s 
%(levelname)s %(levelno)s %(lineno)d %(message)s %(module)s 
%(msecs)d %(name)s %(pathname)s %(process)d %(processName)s 
%(relativeCreated)d %(thread)d %(threadName)s \n''')

show_log()