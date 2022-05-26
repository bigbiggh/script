# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time

class TesttsPipeline:
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'ZH' + now + '.txt'
        with open(fileName, 'a') as fp:
            for url in item['url']:
                fp.write(url+'\n')
        return item
