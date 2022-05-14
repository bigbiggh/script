from django.contrib import admin
from .models import Article
# Register your models here.
"""模型注册进admin里面"""
admin.site.register(Article)