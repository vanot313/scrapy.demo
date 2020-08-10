# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerScrapyItem(scrapy.Item):
    # TODO 根据需求更改提取的数据格式
    name = scrapy.Field()
    url = scrapy.Field()
