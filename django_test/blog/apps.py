from django.apps import AppConfig

"""初始化文件之后自动创建的文件，应用的配置"""


class BlogConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
