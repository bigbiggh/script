步骤1：scrapy startproject getProxy        初始化项目目录
步骤2：scrapy shell https://weather.cma.cn     查看返回response是否可以200
步骤3：浏览器打开想要爬取的网页对应的元素




只需要修改四个文件
items.py    决定爬取哪些项目;填空。。。
settings.py  决定由谁处理爬取的内容
pipelines.py    决定爬取的内容怎么处理
wuHanMovieSpider.py     决定怎么爬