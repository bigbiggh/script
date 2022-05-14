# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/12 16:25
# @Author   :Administrator
# @File :pipelines.py
# @Description:扫尾
# ------------------------------
import time


class TestMoviePipeline:
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'wuHan' + now + '.txt'
        with open(fileName, 'a') as fp:
            fp.write(item['movieName'][0] + '\n\n')
        return item
