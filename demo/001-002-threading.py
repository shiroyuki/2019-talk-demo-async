from logging import getLogger, StreamHandler, DEBUG
import time
import threading
from typing import Any, Dict

logger = getLogger(__name__)
logger.setLevel(DEBUG)
log_handler = StreamHandler()
log_handler.setLevel(DEBUG)
logger.addHandler(log_handler)


def func_001(shared_memory: Dict[str, str], key: str):
    logger.debug('func_001: start')
    time.sleep(2)
    # raise RuntimeError('Panda')
    shared_memory[key] = 'r001'
    logger.debug('func_001: end')


def func_002(shared_memory: Dict[str, str], key: str):
    logger.debug('func_002: start')
    time.sleep(2)
    shared_memory[key] = 'r002'
    logger.debug('func_002: end')


def main():
    logger.debug('main: start')
    shared_memory = dict()
    t1 = threading.Thread(target=func_001, args=(shared_memory, 'p001'))
    t2 = threading.Thread(target=func_002, args=(shared_memory, 'p002'))
    logger.debug('main: threads start')
    t1.start()
    t2.start()
    logger.debug('main: threads joining')
    t1.join()
    t2.join()
    logger.debug('main: threads joined')
    logger.debug(f'main: p001 = {shared_memory["p001"]}')
    logger.debug(f'main: p002 = {shared_memory["p002"]}')
    logger.debug('main: exit')

if __name__ == '__main__':
    main()
