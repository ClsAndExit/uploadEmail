# coding:utf-8
#@Time    :2019/3/31 15:39
from util.email_toolkit import run_ing
from util.conf_toolkit import ConfigManager
from util.log_toolkit import get_logger_by_name
import sys
import time
import pandas as pd
logger = get_logger_by_name(__file__)
try_times = 1

while True:
    logger.info("start try the {} times".format(try_times))
    try_times += 1
    try:
        run_ing()
    except:
        logger.exception(sys.exc_info())
    time.sleep(20)