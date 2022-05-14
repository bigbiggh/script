# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/14 10:25
# @Author   :Administrator
# @File :pipelines2json.py
# @Description:
# ------------------------------
import time,json,codecs

class TestWeatherPipeline(object):
    def process_item(self,item,spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = today + '.json'
        with codecs.open(fileName, 'a') as fp:
            line = json.dumps(dict(item),ensure_ascii=False)+'\n'
            fp.write(line)
        return item