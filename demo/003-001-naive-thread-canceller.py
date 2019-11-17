from logging import getLogger, StreamHandler, DEBUG
from threading import Thread, _shutdown
from time import sleep
from traceback import print_exc

logger = getLogger(__name__)
logger.setLevel(DEBUG)
log_handler = StreamHandler()
log_handler.setLevel(DEBUG)
logger.addHandler(log_handler)

t0: Thread = None
stdout = logger.debug


def worker():
    while True: sleep(1)


def runner():
    global t0

    t0 = Thread(target=worker, daemon=False)
    t0.start()
    sleep(4)
    if t0.is_alive():
        t0.join(timeout=5)
        stdout('[Runner] t0 just joined back.')
    else:
        stdout('[Runner] t0 is already dead before the stopper comes.')


def interceptor():
    global t0

    sleep(2)
    try: t0._stop()
    except: print_exc()


t_runner = Thread(target=runner)
t_interceptor = Thread(target=interceptor)
t_runner.start()
t_interceptor.start()
t_runner.join()
t_interceptor.join()
