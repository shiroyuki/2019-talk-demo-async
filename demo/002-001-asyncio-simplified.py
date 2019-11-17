import asyncio
from logging import getLogger, StreamHandler, DEBUG
import time
from typing import Any, List, Dict

logger = getLogger(__name__)
logger.setLevel(DEBUG)
log_handler = StreamHandler()
log_handler.setLevel(DEBUG)
logger.addHandler(log_handler)


async def func_001():
    await asyncio.sleep(3)
    return 'r001'


async def func_002():
    await asyncio.sleep(2)
    return 'r002'


async def main():
    logger.debug('main: start')
    p001, p002 = await asyncio.gather(func_001(),
                                      func_002())
    logger.debug(f'main: p001 = {p001}')
    logger.debug(f'main: p002 = {p002}')
    logger.debug('main: exit')

if __name__ == '__main__':
    asyncio.run(main())
