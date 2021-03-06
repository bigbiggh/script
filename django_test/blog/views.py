from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog.models import Article


def hello_world(request):
    return HttpResponse("hello world")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    article_date = article.publish_date
    return_str = "title：{},brief_content：{},content：{},article_id：{},article_date：{}".format(title,
                                                                                             brief_content,
                                                                                             content,
                                                                                             article_id,
                                                                                             article_date)
    return HttpResponse(return_str)


# 视图函数
def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html',
                  {
                      'article_list': all_article
                  }
                  )


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    # print(all_article)
    curr_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break

    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article

                  }
                  )
