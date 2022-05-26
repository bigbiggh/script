import scrapy

from TS.items import TsItem
from scrapy.selector import Selector

class TsspiderSpider(scrapy.Spider):
    name = 'TSspider'
    allowed_domains = ['tangshan.creb.com.cn']
    start_urls = ['http://tangshan.creb.com.cn/cj-1.html']

    def parse(self,response):
        subSelector = response.xpath('/html/body/div[2]/div/div[2]/div[1]')
        # subSelector = response.xpath('/html/body/div[2]/div/div[2]/div[1]/div[6]/div/div/div[1]/div')  # response请求网页后返回的数据
        print(subSelector)
        # 选取节点 subSelector
        items = []

        # 解析下级标签出来
        for sub in subSelector:
            item = TsItem()
            item['url'] = sub.xpath('./a/@href').extract()
            items.append(item)
        return items