# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/17 11:46
# @Author   :Administrator
# @File :mylog.py
# @Description:
# ------------------------------
import logging
import getpass
import sys


# 定义类
class MyLog(object):
    '''这个类用于创建一个自用的log'''

    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)

        self.logfile = sys.argv[0][0:-3] + '.log'  # 日志文件名
        self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')
        '''日志显示到屏幕上并输出到日志文件内'''
        self.logHand = logging.FileHandler(self.logfile,encoding='utf-8')
        self.logHand.setFormatter(self.formatter)
        self.logHand.setLevel(logging.DEBUG)  # 只有错误才会被记录到logfile中

        self.logHandst = logging.StreamHandler()
        self.logHandst.setFormatter(self.formatter)
        self.logHandst.setLevel(logging.DEBUG)

        self.logger.addHandler(self.logHand)
        self.logger.addHandler(self.logHandst)

    '''日志的5个级别对应以下的5个函数'''

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

