import scrapy

from PytestLearn.getProxy.getProxy.items import GetproxyItem


class XicispiderSpider(scrapy.Spider):
    name = 'xiciSpider'
    allowed_domains = ['www.66ip.cn']
    start_urls = ['http://www.66ip.cn/']

    def parse(self, response):
        subSelector = response.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tbody/')
        items = []
        for sub in subSelector:
            item = GetproxyItem()
            item['ip'] = sub.xpath('./tr/td[1]/text()').extract()
            item['port'] = sub.xpath('./tr/td[2]/text()').extract()
            item['location'] = sub.xpath('./tr/td[3]/text()').extract()
            item['type'] = sub.xpath('./tr/td[4]/text()').extract()
            # item['name'] = sub.xpath('./tr/td[5]/text()').extract()[0]
            item['protocol'] = 'HTTP'
            item['source'] = '66daili'
            items.append(item)
        return items
