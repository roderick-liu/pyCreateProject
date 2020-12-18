#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from loguru import logger
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_file_path = os.path.join(BASE_DIR, 'log/my.log')
err_log_file_path = os.path.join(BASE_DIR, 'log/err.log')


def get_log():
    logger.add(sys.stderr, format="{time} {level} {message}",
               filter="my_module", level="INFO")
    # Automatically rotate too big file
    logger.add(log_file_path, rotation="500 MB", encoding='utf-8',
               level='DEBUG', retention='10 days')
    logger.add(err_log_file_path, rotation="500 MB", encoding='utf-8',
               level='ERROR')

    #logger.add(err_log_file_path, compression='zip')
    return logger


# if __name__ == '__main__':
    # log = get_log()
    # log.info("lddldlnew")
    # log.error("error")
    # log.debug("dknew")
