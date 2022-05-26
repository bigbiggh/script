import scrapy
from testTS.items import TesttsItem


class TsspiderspiderSpider(scrapy.Spider):
    name = 'TSspiderSpider'
    allowed_domains = ['www.creb.com.cn']
    start_urls = ['http://tangshan.creb.com.cn/cj-1.html']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://tangshan.creb.com.cn/cj-1.html',
        }
        # 指定cookies
        cookies = {'_site_id_cookie': '42',
                   'clientlanguage': 'zh_CN', 'Hm_lvt_0a68072ef88a48311cbc5335e43e6895': '1653464530; ',
                   'Hm_lvt_05e80175384ce890c37e0f9e659bc0f2': '1653464530; ',
                   'Hm_lvt_f47251632f3a09d18505f3fc6d6bab93': '1653464530; ',
                   'acw_tc': '2760827116535297571316704e6e93752f7fae8a98ca92616cc6f750cb18be; ',
                   'JSESSIONID': '7DE7EEDAC4FFE4384E5A99A3C4B27111',
                   'Hm_lpvt_05e80175384ce890c37e0f9e659bc0f2': '1653529759; ',
                   'Hm_lpvt_f47251632f3a09d18505f3fc6d6bab93': '1653529759; ',
                   'acw_sc__v2': '628edcc59d2a0c74e1694be2b4aeb5c9268cc2e0; ',
                   'Hm_lpvt_0a68072ef88a48311cbc5335e43e6895': '1653529798 '
                   }
        urls = [
            'http://tangshan.creb.com.cn/cj-1.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        subSelector = response.xpath(
            '/html/body/div[2]/div/div[2]/div[1]/div[6]/div/div/div[1]')  # response请求网页后返回的数据
        # 解析下级标签
        items = []
        for sub in subSelector:
            item = TesttsItem()
            item['url'] = sub.xpath('./div/a/@href').extract()
            items.append(item)

        return items
