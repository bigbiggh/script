# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/5/16 15:46
# @Author   :Administrator
# @File :test.py
# @Description:
# ------------------------------
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('scenery.html',encoding='Utf-8'),'lxml')
print(soup.prettify())
print(soup.find('a',attrs={'class':'price'}))

# with open('scenery.html',encoding='Utf-8') as p:
#     p.read()