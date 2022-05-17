# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/16 15:35
# @Author   :Administrator
# @File :customProxy.py
# @Description:
# ------------------------------
from PytestLearn.testWeather.testWeather.middlewares.resource import PROXIES
import random
class RandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = 'http://%s' %proxy
