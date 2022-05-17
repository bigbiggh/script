# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time

class GetproxyPipeline:
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'Xian' + today + '.txt'

        with open(fileName, 'a') as fp:
            for ip in item['ip']:
                fp.write(ip + '\t')
                fp.write(item['port'] + '\t')
                fp.write(item['location'] + '\t')
                fp.write(item['type'] + '\t')
                fp.write(item['name'] + '\t')
                fp.write(item['source'] + '\n')
                time.sleep(1)
        return item
