# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/20 11:48
# @Author   :Administrator
# @File :bugtargetTest.py
# @Description:
# ------------------------------
import requests,os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Target:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def send_input(self,ele,value):
        ele.click()
        ele.clear()
        ele.send_keys(value)
    def login(self):
        login_ul = "https://www.damai.cn/"
        username = "13289380807"
        password = "Gh@970422"
        self.driver.get(login_ul)
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div[1]/div[1]/span").click()
        u = self.driver.find_element(By.XPATH,'//*[@id="fm-login-id"]')
        self.send_input(u, username)
        p = self.driver.find_element(By.ID,'//*[@id="fm-login-password"]')
        self.send_input(p, password)

        targer_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.591b23e1pwOo9p&id=670586984056'
        self.driver.get(targer_url)
if __name__ == '__main__':
    T = Target()
    T.login()