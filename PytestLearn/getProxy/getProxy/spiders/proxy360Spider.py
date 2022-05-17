# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/14 13:50
# @Author   :Administrator
# @File :proxy360Spider.py
# @Description:
# ------------------------------
import scrapy
from PytestLearn.getProxy.getProxy.items import GetproxyItem


class Proxy360Spider(scrapy.Spider):
    name = 'proxy360Spider'
    allowed_domains = ["proxy-checker.net"]
    start_urls = ['https://proxy-checker.net/cn/free-proxy/']

    def parse(self, response):
        subSelector = response.xpath('//*[@id="js-free-proxy-table"]/tbody')
        items = []
        for sub in subSelector:
            item = GetproxyItem()
            item['ip'] = sub.xpath('./tr/td[1]/text()').extract()
            item['port'] = sub.xpath('./tr/td[2]/text()').extract()
            item['location'] = sub.xpath('./tr/td[3]/text()').extract()
            item['type'] = sub.xpath('./tr/td[4]/text()').extract()
            item['name'] = sub.xpath('./tr/td[5]/text()').extract()
            item['protocol'] = 'HTTP'
            item['source'] = 'proxy360'
            items.append(item)
            print(items)

        return items
