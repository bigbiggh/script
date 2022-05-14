# -*- coding:utf-8-*-

import urllib3,re
from scrapy.selector import Selector

class Urllib3:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def download(self, func,url):
        print("download url:", url)
        try:
            html = self.http.request(func, url,timeout = 4.0)
        except urllib3.exceptions as e:
            print("download error:", e)
        return html.data
if __name__ == '__main__':
    x = Urllib3().download("get","https://www.cnblogs.com/eliwang/p/14284091.html").decode()
    # y = x.replace(' ','').replace('\n','').replace('\r','')
    # re_y = re.compile(r'</head>(.*)</body>').findall(y)
    y = Selector(text='body').xpath('//*').extract()
    # print(x)
    print(y)
