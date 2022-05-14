from django.db import models


# Create your models here.
class Article(models.Model):
    # 文章标题
    title = models.TextField()
    # 摘要
    brief_content = models.TextField()
    # 唯一ID
    article_id = models.AutoField(primary_key=True)
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True)
    # 内容
    content = models.TextField()

    # 文章以标题title显示
    def __str__(self):
        return self.title
