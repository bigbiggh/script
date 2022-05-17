# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/17 11:40
# @Author   :Administrator
# @File :getCommentInfo.py
# @Description:
# ------------------------------
import string
import urllib.request
from bs4 import BeautifulSoup
from mylog import MyLog as mylog
from urllib.parse import quote


class Item(object):
    title = None
    firstAuthor = None
    firstTime = None
    reNum = None
    content = None
    lastAuthor = None
    lastTime = None


class GetTiebaInfo(object):
    def __init__(self, url):
        self.url = url
        self.log = mylog()
        self.pageSum = 5
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def getUrls(self, pageSum):
        urls = []
        pns = [str(i * 50) for i in range(pageSum)]
        ul = self.url.split('=')
        for pn in pns:
            ul[-1] = pn
            url = '='.join(ul)
            urls.append(url)
        self.log.info(u'获取URLS成功')
        return urls

    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getReponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tagsli = soup.find_all('div', attrs={'class': 't_con cleafix'})
            # print(tagsli)
            for tag in tagsli[3:]:
                item = Item()
                item.title = tag.find('a', attrs={'class': 'j_th_tit'}).get_text().strip()
                item.firstAuthor = tag.find('span', attrs={'class': 'frs-author-name-wrap'}).get_text().strip()
                # print(item.firstAuthor)
                item.firstTime = tag.find('span', attrs={'title': u'创建时间'}).get_text().strip()
                item.reNum = tag.find('span', attrs={'title': u'回复'}).get_text().strip()
                item.content = tag.find('div',
                                        attrs={'class': 'threadlist_abs threadlist_abs_onlyline'}).get_text().strip()
                # item.lastAuthor = tag.find('span', attrs={'class': 'tb_icon_author_rely j_replayer'}).get_text().strip()
                item.lastTime = tag.find('a', attrs={'class': 'j_th_tit'}).get_text().strip()
                items.append(item)
        return items

    def pipelines(self, items):
        fileName = 'baidutieba.txt'.encode('utf-8')
        with open(fileName, 'a', encoding='utf-8') as fp:
            for item in items:
                fp.write('title:%s \t author:%s \n firstTime:%s \t content":%s \t return:%s \t '
                         'lastTime:%20s \n\n\n' % (item.title,item.firstAuthor,item.firstTime,item.reNum,
                                                   item.content,item.lastTime
                ))
                self.log.info(u'标题为<<%s>>的项输入到"%s"成功' % (item.title, fileName.decode('utf-8')))

    def getReponseContent(self, url):
        # response = ''
        # try:
        url1 = quote(url, safe=string.printable)
        response = urllib.request.urlopen(url1).read()

        # except:
        #     print('error')
        return response
        # response = http.request('GET', url.encode('utf-8'))
        # except:
        #     self.log.error('Python 返回URL:%s 数据失败' % url)
        # else:
        #     self.log.error('Python 返回URL:%s 数据失败' % url)
        #     return response


if __name__ == '__main__':
    url = u'http://tieba.baidu.com/f?kw=权力的游戏&ie=utf-8&pn=0'
    GTI = GetTiebaInfo(url)
