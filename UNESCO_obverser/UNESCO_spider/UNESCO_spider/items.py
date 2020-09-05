# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#世界遗产详情
class UnescoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    detail = scrapy.Field()
    img_src = scrapy.Field()
    country_name = scrapy.Field()
    time = scrapy.Field()

#世界遗产国家列表
class UnescocountryspiderItem(scrapy.Item):
    country_name = scrapy.Field()

class UnescokindspiderItem(scrapy.Item):
    kind = scrapy.Field()
    name = scrapy.Field()

class UnesconewsItem(scrapy.Item):
    name = scrapy.Field()
    time = scrapy.Field()
    Detail = scrapy.Field()
    img_src = scrapy.Field()
    sdetail = scrapy.Field()
    dsrc = scrapy.Field()
    year = scrapy.Field()