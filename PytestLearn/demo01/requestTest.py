# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/19 11:24
# @Author   :Administrator
# @File :requestTest.py
# @Description:
# ------------------------------
# import os
# import pickle
#
# from selenium import webdriver
# import time
#
# # 大麦网主页
# from selenium.webdriver.common.by import By
#
# damai_url = "https://www.damai.cn/"
# # 登录页
# login_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
# # 抢票目标页
# target_url = 'https://buy.damai.cn/orderConfirm?exParams=%7B%22damai%22%3A%221%22%2C%22channel%22%3A%22damai_app%22%2C%22umpChannel%22%3A%2210002%22%2C%22atomSplit%22%3A%221%22%2C%22serviceVersion%22%3A%221.8.5%22%2C%22umidToken%22%3A%22T2gAtPyCjg_AUWoyiecLDTrmKyHb3z0AgG_eGei1zIyqxm-jthwfnK6YOe6f82zH400%3D%22%2C%22ua%22%3A%22140%23C6SoUsIHzzP%2BfQo22xu%2BwpN8s7a3up99i0JcsaaXRCS8yOkVK%2FiqUSbPHHCBzRE8R4xgZanLHdF3ZKINXoM4A3hqzznbRRyZmPQzzF8HIamqlQzx2DD3VthqzFdQ2XU%2BllfzzPziVW2ndu8I1Cr8jMbjNv%2F5HvNy45ML%2B7GkviKiOkZHGiYO14xNkpsrMRWj3%2BxffgchKrBtv5OI0ywFywcSyD%2BvFIVBKuFasA%2FWndunik4HMLfw7LeMFQz261Eu2aCfbNrTW9yw%2BWr6VQgcIsVkXIBzUuU9mkkRXY8jmUMq5K%2BTjovXmZQEEyVFlX7UGKE4ZX1jzQWpK10hJ61408l2VlVV%2FHHZlBWXRemsJFfHBT%2FSuxqGfUvvZjiQPlTFS%2FyaWFnxX4Cq4JoRnfhcz5CeLlQ6OEpd3h3taFzuFcsRRWWg9jEO8wzLtokUTPJIvLpD%2FoGwWYNLzZMVj9NPsbvaIqGDQeVUAPR2RmzT1IbSCxGarujZ8k1GlD44NlljMqHTountpzu0l4D0l%2BhI5x6AZ7b606%2B2%2BmZwzmSUTTeBIJV8M6GOLq53VAMuAUWgWUNfRjS1GzF0151dKh8l6BEbSYR5IYdTM3vtl3%2BJXHprX4fwfoxeJ4WW1uHu4WS5vN%2B4CweozYoIxhf9Lz%2FGaJ2gsEHRK6wL3DdyW0Kdkf%2F8BGxGZ4kcO4ELylVKnCmskZBpeB1MJXUekDPWfJ%2FhOfVUe7VEu2i6hLCwbNQlhVG7LztI6b6sy6VUjfDqcfjjXnW23zONqHv2q4HXsw2%2FdKBxVrdDFaK2Z0R%2FnIPaLbiIUw7AiZRs60yNQKkerElqj%2FWoavOKytra7wAcvlQO0oxbZQVeRBnVyClXLUvojyHlKYAFDsvfKYUNDrcHQlpHlb6ykZ4QcL2vwzz%3D%22%7D&buyParam=670586984056_1_4826979556797&buyNow=true&spm=a2oeg.project.projectinfo.dbuy'
#
#
# class Concert:
#     def __init__(self):
#         self.status = 0  # 状态,表示如今进行到何种程度
#         self.login_method = 1  # {0:模拟登录,1:Cookie登录}自行选择登录方式
#         self.driver = webdriver.Chrome()  # 默认Chrome浏览器
#         self.driver.maximize_window()
#
#     def set_cookie(self):
#         self.driver.get(damai_url)
#         print("###请点击登录###")
#         while self.driver.title.find('大麦网-全球演出赛事官方购票平台') != -1:
#             time.sleep(1)
#         print('###请扫码登录###')
#
#         while self.driver.title != '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
#             time.sleep(1)
#         print("###扫码成功###")
#         pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
#         print("###Cookie保存成功###")
#         self.driver.get(target_url)
#
#     def get_cookie(self):
#         try:
#             cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
#             for cookie in cookies:
#                 cookie_dict = {
#                     'domain': '.damai.cn',  # 必须有，不然就是假登录
#                     'name': cookie.get('name'),
#                     'value': cookie.get('value')
#                 }
#                 self.driver.add_cookie(cookie_dict)
#             print('###载入Cookie###')
#         except Exception as e:
#             print(e)
#
#     def login(self):
#         if self.login_method == 0:
#             self.driver.get(login_url)
#             # 载入登录界面
#             print('###开始登录###')
#
#         elif self.login_method == 1:
#             if not os.path.exists('cookies.pkl'):
#                 # 如果不存在cookie.pkl,就获取一下
#                 self.set_cookie()
#             else:
#                 self.driver.get(target_url)
#                 self.get_cookie()
#
#     def enter_concert(self):
#         """打开浏览器"""
#         print('###打开浏览器，进入大麦网###')
#         # self.driver.maximize_window()           # 最大化窗口
#         # 调用登陆
#         self.login()  # 先登录再说
#         self.driver.refresh()  # 刷新页面
#         self.status = 2  # 登录成功标识
#         print("###登录成功###")
#         # 后续德云社可以讲
#         if self.isElementExist('/html/body/div[2]/div[2]/div/div/div[3]/div[2]'):
#             self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div[2]').click()
#
#     def choose_ticket(self):
#         if self.status == 2:  # 登录成功入口
#             print("=" * 30)
#             print("###开始进行日期及票价选择###")
#             while self.driver.title.find('确认订单') == -1:  # 如果跳转到了订单结算界面就算这步成功了，否则继续执行此步
#                 try:
#                     buybutton = self.driver.find_element(By.CLASS_NAME, 'buybtn').text
#                     if buybutton == "提交缺货登记":
#                         # 改变现有状态
#                         self.status = 2
#                         self.driver.get(target_url)
#                         print('###抢票未开始，刷新等待开始###')
#                         continue
#                     elif buybutton == "立即预定":
#                         self.driver.find_element(By.CLASS_NAME, 'buybtn').click()
#                         # 改变现有状态
#                         self.status = 3
#                     elif buybutton == "立即购买":
#                         self.driver.find_element(By.CLASS_NAME, 'buybtn').click()
#                         # 改变现有状态
#                         self.status = 4
#                     # 选座购买暂时无法完成自动化
#                     elif buybutton == "选座购买":
#                         self.driver.find_element(By.CLASS_NAME, 'buybtn').click()
#                         self.status = 5
#                 except:
#                     print('###未跳转到订单结算界面###')
#                 title = self.driver.title
#                 if title == '选座购买':
#                     # 实现选座位购买的逻辑
#                     self.choice_seats()
#                 elif title == '确认订单':
#                     while True:
#                         # 如果标题为确认订单
#                         print('waiting ......')
#                         if self.isElementExist('//*[@id="container"]/div/div[9]/button'):
#                             self.check_order()
#                             break
#
#     def choice_seats(self):
#         while self.driver.title == '选座购买':
#             while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img'):
#                 # 座位手动选择 选中座位之后//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img 就会消失
#                 print('请快速的选择您的座位！！！')
#             # 消失之后就会出现 //*[@id="app"]/div[2]/div[2]/div[2]/div
#             while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[2]/div'):
#                 # 找到之后进行点击确认选座
#                 self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/button').click()
#
#     def check_order(self):
#         if self.status in [3, 4, 5]:
#             print('###开始确认订单###')
#             try:
#                 # 默认选第一个购票人信息
#                 self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[1]/div/label').click()
#             except Exception as e:
#                 print("###购票人信息选中失败，自行查看元素位置###")
#                 print(e)
#             # 最后一步提交订单
#             time.sleep(0.5)  # 太快会影响加载，导致按钮点击无效
#             self.driver.find_element_by_xpath('//div[@class = "w1200"]//div[2]//div//div[9]//button[1]').click()
#
#     def finish(self):
#         self.driver.quit()
#
#     def isElementExist(self, element):
#         flag = True
#         driver = self.driver
#         try:
#             driver.find_element(By.XPATH, element)
#             return flag
#         except:
#             flag = False
#             return flag
#
#
# if __name__ == '__main__':
#     try:
#         con = Concert()  # 具体如果填写请查看类中的初始化函数
#         con.enter_concert()  # 打开浏览器
#         # con.choose_ticket()         # 开始抢票
#
#     except Exception as e:
#         print(e)
#         con.finish()
# header = {
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#     "Connection": "keep-alive",
#     "Content-Length": "2",
#     "Content-Type": "application/json",
# }
import requests,re


def get_token():
    url = "http://192.168.1.203:7777/mes/cloud/v1/auth/oauth/token?grant_type=password&username=admin&password=123&scope=app&client_id=mes-app&client_secret=AE02C169AC75470319AD1B12282E5C61"
    data = {"username": "admin", "password": "123"}
    response = requests.request("post", url, data=data)
    response_dict = eval(response.text)
    return response_dict['access_token']

get_token()

#     '''
#     description:        get_api_res
#                         获取对应接口messageCode;
#     '''
#     @classmethod
def get_api_res(func, url):
    API_info = {
        "headers":
            {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Authorization": "Bearer %s" % get_token(),
                "Connection": "keep-alive",
                "Content-Type": "application/json; charset=UTF-8"
            },
        "payload": "{\"exported\":false,\"paging\":{\"page\":1,\"size\":12,\"sortings\":[]}}"
    }
    response = requests.request(func, url=url, headers=API_info["headers"], data=API_info["payload"])
    response_json = response.json()
    return response_json
#
if __name__ == '__main__':
    url = "http://192.168.1.203:7777/mes/cloud/v1/module/product/api/tool/fc/saveOrUpdate"
    msg = get_api_res("POST",url)
    for i in msg:
        print(msg)


