# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/12 16:25
# @Author   :Administrator
# @File :items.py
# @Description:定义爬虫需要哪些项
# ------------------------------
import scrapy


class TestMovieItem(scrapy.Item):
    movieName = scrapy.Field()  # 电影名字
