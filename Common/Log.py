# -*- coding: utf-8 -*-
# @Author : Joy

import logging
import os
import time

# 输入日志思路
# 1、创建一个logger
# 2、创建一个handler，用于写入日志文件
# 3、定义handler的输出格式
# 4、将logger添加到handler中
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}

logger = logging.getLogger()
level = 'default'


def create_file(filename):
    # 返回filename所在目录
    path = filename[0: filename.rfind('/')]
    # filename不存在则创建
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fp = open(filename, mode='w', encoding='utf-8')
        fp.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.err_handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.err_handler)


def get_current_time():
    return time.strftime(MyLog.date, time.localtime(time.time()))


class MyLog(object):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/Log/log.log'
    err_file = path + '/Log/err.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)

    date = '%Y-%m-%d %H:%M:%S'
    log_handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(log_file, encoding='utf-8')

    @staticmethod  # 定义静态函数
    def debug(log_msg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + log_msg)
        remove_handler('debug')

    @staticmethod
    def info(log_msg):
        set_handler('info')
        logger.debug("[INFO " + get_current_time() + log_msg)
        remove_handler('info')

    @staticmethod
    def warning(log_msg):
        set_handler('warning')
        logger.debug("[WARNING " + get_current_time() + log_msg)
        remove_handler('warning')

    @staticmethod
    def error(log_msg):
        set_handler('error')
        logger.debug("[ERROR " + get_current_time() + log_msg)
        remove_handler('error')

    @staticmethod
    def critical(log_msg):
        set_handler('critical')
        logger.debug("[CRITICAL " + get_current_time() + log_msg)
        remove_handler('critical')


if __name__ == '__main__':
    MyLog.debug('This is debug message!')
    MyLog.info('This is info message!')
    MyLog.warning('This is warning message!')
    MyLog.error('This is error message!')
    MyLog.critical('This is critical message!')
