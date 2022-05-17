# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Meiju100Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cityDate = scrapy.Field()  # 电影名字
    img = scrapy.Field()
    min_temperature = scrapy.Field()
    max_temperature = scrapy.Field()
    weather = scrapy.Field()
