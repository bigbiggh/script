# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/12 16:26
# @Author   :Administrator
# @File :settings.py
# @Description:上层目录总scrapy.cfg定义的设置文件
# ------------------------------
BOT_NAME = 'testWeather'

SPIDER_MODULES = ['testWeather.spiders']

NEWSPIDER_MODULE = 'testWeather.spiders'

ITEM_PIPELINES = {'testWeather.pipelines.TestWeatherPipeline': 1}

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"