# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/20 14:18
# @Author   :Administrator
# @File :pandasTest.py
# @Description:
# ------------------------------
import pandas as pd
df_excel = pd.read_excel("../../TestData.xlsx",sheet_name="Sheet1")
# print(df_excel.head())
# 会话式编程保存多个sheet数据到同一个excel中
# writer = pd.ExcelWriter()
# df_excel.to_excel(writer,"sheet")

# with pd.ExcelWriter("测试保存会话式保存多个") as writer:
#     df_excel.to_excel(writer,sheet_name="sheet3")



# 保存csv
df_excel.to_csv('测试保存csv.csv')