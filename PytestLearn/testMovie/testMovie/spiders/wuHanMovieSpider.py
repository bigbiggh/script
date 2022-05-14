'''scrapy genspider wuHanMovieSpider jycinema.com命令创建的爬虫文件'''

import scrapy
from PytestLearn.testMovie.testMovie.items import TestMovieItem
from scrapy import Selector


class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'WuhanmoviespiderSpider'  # 爬虫名
    allowed_domains = ['jycinema.com']  # 定义域范围
    start_urls = ['https://www.iqiyi.com']  # 爬虫的网页；元组
    def parse(self,response):
        subSelector = response.xpath('//*[@id="adSkinInner"]/div[4]/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/ul/li')  # response请求网页后返回的数据
        # 选取节点 subSelector
        items = []
        # 解析下级标签出来
        for sub in subSelector:
            item = TestMovieItem()
            item['movieName'] = sub.xpath('./div/div[2]/p[1]/a/span/text()').extract()
            items.append(item)
        return items
