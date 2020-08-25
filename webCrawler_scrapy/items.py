# -*- coding: utf-8 -*-


import scrapy


class WebcrawlerScrapyItem(scrapy.Item):
    # TODO 根据需求更改提取的数据格式
    # 数据表名
    tablename = "testpictures"
    # 表属性类型
    attributetypes = ("%s", "%s")
    # 表属性名
    attributenames = ("t_name", "t_url")
    # 数据实体
    t_name = scrapy.Field()
    t_url = scrapy.Field()

class SecurityItem(scrapy.Item):
    tablename = "testpictures"
    attributetypes = ("%s", "%s")
    attributenames = ("t_name", "t_url")
