# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/21 15:37
# @Author   :Administrator
# @File :urls.py.py
# @Description:应用层次路由配置
# ------------------------------
from django.urls import path
import blog.views

"""
    如果path有hello_world，则转发到blog.views.hello_world
"""
urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page),
    # path('detail', blog.views.get_detail_page),
    path('detail/<int:article_id>', blog.views.get_detail_page)

]
