import scrapy
from testTS.items import TesttsItem

class ZHspiderspiderSpider(scrapy.Spider):
    name = 'ZHspiderSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/search?q=%E6%B5%B7%E5%8D%97']

    def start_requests(self):
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'x-requested-with': 'fetch',
            'Referer': 'https://www.zhihu.com/search?q=%E6%B5%B7%E5%8D%97&range=1d&type=content',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
        }
        cookies = {'_zap': '97300fae-4fa6-4d8c-b82a-49d21867c44f',
                   '_xsrf': '690efc97-7380-4772-b1bd-82ed28012761',
                   'd_c0': "AaAd6_Hd5BSPTlzX2_iRdOM2-8bVfAkJh04=|1651736386",
                   'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1651736387',
                   '_9755xjdesxxd_': '32',
                   'YD00517437729195%3AWM_TID': 'VR%2FlWLgRIGBEUQEFQEKUUYZeGdZZbY9V',
                   '__snaker__id': 'CwizyYEWdCBur6Eh',
                   'gdxidpyhxdE': 'y8mS8tLORZ%2BoPbbt0N%2F7kAEGNYYBZKnBIxUcwH'
                                  '%2FD69VdW9SXCEl6t7YMTNVVtsM22621u88fnIVbdHmdLRjY2TipPbglGQ64uOIX2aiyqRzw1Q5SnDkg2grJSKCHe%2F8eTGWIxMBrdVGZD3n3O%2BJyXr4h%2BaDuLGsDnuUIaYoi8TgbDYcB%3A1652168041812',
                   'YD00517437729195%3AWM_NI': '2OAPaMAckEPn3d5Xwjl6%2Bh0bmKPz5ONw3Bfd%2FmiGEfOicz6%2FFCTuQ4flRG%2BGW'
                                               '%2FtSWSkXuGh2A%2BsGtIjXvOzTkDntwkpDOeSLySLZNL4nA%2FZE5u4KTGV8oQ9h4Pk7Wkl0cUs%3D',
                   'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee90ee59f8b9a1accc6ea6a88fb3d55b929a8fadc45aa1eeb895e96eb1ae9f8ced2af0fea7c3b92af2918fb1e44783bda5a6d366f1bcfbb9f662b0eae589b36aaf95a09bb8458ea9fda3e570edb3a7a8c86e8db7ad9bb525869d9c96d440a6b49ea8aa4d95f1bcb4d659a988bba8eb3a83f5bda8f743aa88bab0f960a99ca295f661b49c8186d248bb8d84bbcd48f8b28fd0d94ff7abfcacd74d96e8a1b2bc64f890a5d8d661b0f0adb6f237e2a3',
                   'captcha_session_v2': '2|1:0|10:1652167155|18:captcha_session_v2|88'
                                         ':QlEveUc3bllGbXpodGlkVUcvbmR4YW5IR2RkemMycmlrbUpaRFgxTm14TG9oQjJEYXJCc1BUMkh0b2p0b2dPbA==|e42d2607ff7f2d546017d9871368090932d46cb18a1ba93f1a7be7baa1ffc18b',
                   'z_c0': "2|1:0|10:1652167174|4:z_c0|92"
                           ":Mi4xMDY3S0F3QUFBQUFCb0IzcjhkM2tGQ2NBQUFDRUFsVk5CcC1oWWdCNDJxT0hrSF9PV0RXRVl0dWhCalR0T3BHU1FB|bb026e73873523571440d0d4e44437bbdefc7f258f0f28d67658fd590d179893",
                   'q_c1': '2f815a7070cc4befa6c88401faf2bf8c|1652167202000|1652167202000',
                   'tst': 'r',
                   'SESSIONID': 'rFOlobBSIztlKr21dsJFFh8ytHcmvDo7BQTixKBuRyr',
                   'JOID': 'U1ocBE--2D237jSgXrhuqDsX70JCz5V82IRV6QPyoULVpkORZNvpv9PoPKVTVROok4SQyS2BYGa047MD7kaxpZw=',
                   'osd': 'UVsQA0282TGw7DahUr9sqjob6EBAzpl72oZU5QTwo0PZoUGTZdfuvdHpMKJRVxKklIaSyCGGYmS177QB7Ee9op4=',
                   'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1653555169',
                   'NOT_UNREGISTER_WAITING': '1',
                   'KLBRSID': '5430ad6ccb1a51f38ac194049bce5dfe|1653556050|1653550906'
                   }
        urls = [
            'https://www.zhihu.com/search?q=%E6%B5%B7%E5%8D%97&range=1d&type=content'
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        subSelector = response.xpath(
            '//*[@id="SearchMain"]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/h2/span/div/a/span/text()')  # response请求网页后返回的数据
        # 解析下级标签
        items = []
        for sub in subSelector:
            item = TesttsItem()
            item['url'] = sub.xpath('./div/a/@href').extract()
            items.append(item)
        return items
