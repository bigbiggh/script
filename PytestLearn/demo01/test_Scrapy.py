import requests,re

urls = 'https://www.zhihu.com/search?q=%E6%B5%B7%E5%8D%97&type=content'
# data = {
#     'q': '海南',
#     'range': 1,
#     'type': 'content'
# }
headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Content-Encoding': 'gkb',
            # 'Content-Length': 363,
            'Content-Type': 'application/x-protobuf',
            'Referer': 'https://www.zhihu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'

        }
rep = requests.post(urls,headers=headers)
rep.encoding = 'utf-8'
text = rep.text
print(text)