# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/12 16:25
# @Author   :Administrator
# @File :pipelines.py
# @Description:扫尾
# ------------------------------
import time
import os.path
from urllib.request import urlopen


class TestWeatherPipeline:
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'Xian' + today + '.txt'

        with open(fileName, 'a') as fp:
            for cityDate in item['cityDate']:
                fp.write(cityDate+'\t')
                fp.write(item['img'][0] + '\t')
                fp.write(item['min_temperature'][0] + '~')
                fp.write(item['max_temperature'][0] + '\t')
                fp.write(item['weather'][0] + '\n')
            time.sleep(1)
        return item
