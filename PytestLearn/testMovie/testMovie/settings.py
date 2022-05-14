# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/12 16:26
# @Author   :Administrator
# @File :settings.py
# @Description:上层目录总scrapy.cfg定义的设置文件
# ------------------------------
BOT_NAME = 'testMovie'

SPIDER_MODULES = ['testMovie.spiders']

NEWSPIDER_MODULE = 'testMovie.spiders'

ITEM_PIPELINES = {'testMovie.pipelines.TestMoviePipeline': 300}
