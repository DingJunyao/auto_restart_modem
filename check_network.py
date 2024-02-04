import os
import time

import dotenv
from ping3 import ping

from loguru import logger
from restart_modem_gui import restart_modem


dotenv.load_dotenv()
CHECK_ADDR_LIST = os.getenv("CHECK_ADDR_LIST").split(",")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL"))


def check_connection_and_restart():
    flag = 0
    for addr in CHECK_ADDR_LIST:
        if ping(addr):
            flag = 1
            logger.info(f'Connect to {addr} success')
            break
    if flag == 0:
        logger.error('Connection error, restarting modem...')
        restart_modem()


def loop():
    while True:
        check_connection_and_restart()
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    loop()