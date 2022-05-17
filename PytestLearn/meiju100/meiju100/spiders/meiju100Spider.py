import scrapy
from PytestLearn.meiju100.meiju100.items import Meiju100Item

class Meiju100spiderSpider(scrapy.Spider):
    name = 'meiju100Spider'
    allowed_domains = ['tianqi.com']  # 定义域范围
    start_urls = ['https://www.tianqi.com/xian/15/']  # 爬虫的网页；元组

    def parse(self, response):
        subSelector = response.xpath()
        items=[]

        # 解析下级标签出来
        for sub in subSelector:
            item = Meiju100Item()
            item['cityDate'] = sub.xpath('li/a/div[1]/span[1]/text()').extract()
            item['img'] = sub.xpath('li/a/div[2]/img').extract()
            item['weather'] = sub.xpath('li/a/div[3]/text()').extract()
            item['min_temperature'] = sub.xpath('li/a/div[4]/span[1]/text()').extract()
            item['max_temperature'] = sub.xpath('li/a/div[4]/span[2]/text()').extract()
            items.append(item)
        return items
