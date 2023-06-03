import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

a = [1, 2, 3, 4, 5]

try:
    print(a[6])
except Exception as e:
    logging.error(e)

logging.info('프로그램 종료!')