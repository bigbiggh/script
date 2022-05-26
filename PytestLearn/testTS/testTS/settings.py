# Scrapy settings for testTS project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:

BOT_NAME = 'testTS'

SPIDER_MODULES = ['testTS.spiders']
NEWSPIDER_MODULE = 'testTS.spiders'

ITEM_PIPELINES = {'testTS.pipelines.TesttsPipeline': 300}

# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'

# COOKIES_ENABLED = False
# DEFAULT_REQUEST_HEADERS= {
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Accept-Language': 'zh-CN,zh;q=0.9',
#             'Connection': 'keep-alive',
#             'Content-Type': 'application/x-protobuf',
#             # 'Referer': 'https://www.zhihu.com/search?q=海南&range=1d&type=content',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
#
# }

