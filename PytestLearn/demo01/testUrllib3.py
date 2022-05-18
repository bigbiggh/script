# -*- coding:utf-8-*-

import urllib3,re
from scrapy.selector import Selector

class Urllib3:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def download(self,url,user_agent='wswp',num_retries=2):
        print("download url:", url)
        headers = {'user_agent':user_agent}
        try:
            html = self.http.request('get', url,headers=headers,timeout = 4.0)
        except urllib3.exceptions as e:
            print("download error:", e)
            html = None
            if num_retries>0:
                if hasattr(e,'code') and 500<=e.code<600:
                    return self.download(url,user_agent,num_retries)
        # print(html.data)
        return html.data

    def crawl_sitemap(self, url):
        sitemap = self.download(url)
        sitemap = sitemap.decode('ISO-8859-1')
        # print(type(sitemap))
        links = re.findall('<loc>(.*?)</loc>',sitemap)
        for link in links:
            html = self.download(link)
            return html
if __name__ == '__main__':
    url = "http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi"
    html = Urllib3().crawl_sitemap(url)
    print(html)
    # y = x.replace(' ','').replace('\n','').replace('\r','')
    # re_y = re.compile(r'</head>(.*)</body>').findall(y)
    # Selector(text='body').xpath('//*').extract()
    # print(x)
    # print(y)
