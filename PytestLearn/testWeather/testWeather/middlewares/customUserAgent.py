# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/16 15:22
# @Author   :Administrator
# @File :customUserAgent.py
# @Description:
# ------------------------------

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from PytestLearn.testWeather.testWeather.middlewares.resource import UserAgents
import random

class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(UserAgents)
        request.headers.setdefault('User-Agent',ua)