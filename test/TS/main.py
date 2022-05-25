# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/25 16:33
# @Author   :Administrator
# @File :main.py
# @Description:
# ------------------------------
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('TSspider')  # 你需要将此处的spider_name替换为你自己的爬虫名称
    process.start()
