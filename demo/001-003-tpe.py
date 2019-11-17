from logging import getLogger, StreamHandler, DEBUG
import time
from concurrent.futures import as_completed, Future
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Any, List, Dict

logger = getLogger(__name__)
logger.setLevel(DEBUG)
log_handler = StreamHandler()
log_handler.setLevel(DEBUG)
logger.addHandler(log_handler)


def func_001():
    time.sleep(3)
    # raise RuntimeError('Panda')
    return 'r001'


def func_002():
    time.sleep(2)
    return 'r002'


def main():
    logger.debug('main: start')
    with ThreadPoolExecutor() as pool:
        futures: List[Future] = []
        p001 = pool.submit(func_001)
        p002 = pool.submit(func_002)
        logger.debug(f'main: p001 = {p001.result()}')
        logger.debug(f'main: p002 = {p002.result()}')

        # futures.append(p001)
        # futures.append(p002)
        # for complete_future in as_completed(futures):
        #     logger.debug(f'main: p00? = {complete_future.result()}')
    logger.debug('main: exit')

if __name__ == '__main__':
    main()
