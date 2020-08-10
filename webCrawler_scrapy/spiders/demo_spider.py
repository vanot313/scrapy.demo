# coding=utf-8
import scrapy
import re
import os
import urllib.request
import pymysql
import sys
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request

from webCrawler_scrapy.items import \
    WebcrawlerScrapyItem  # 导入item对应的类，crawlPictures是项目名，items是items.py文件，import的是items.py中的class，也可以import *


class DemoSpider(scrapy.spiders.Spider):
    # TODO 自定义爬虫名，要和settings中的BOT_NAME属性对应的值一致
    name = "demo_spider"

    # TODO 网页爬取起始位置与网页爬取范围
    allowed_domains = ["https://nosec.org"]  # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    start_urls = ["https://nosec.org/home/index/security.html"]  # 开始爬取的地址

    # 该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse
    # TODO 此处主要爬虫处理逻辑
    def parse(self, response):
        # 创建查询对象，HtmlXPathSelector已过时
        se = Selector(response)
        asrc = se.xpath("//*[@id='article-content']/div")
        for i in range(len(asrc)):
            aurl = se.xpath("//*[@id='article-content']/div[%d]/div[2]/a" % i).attrib.get("href")
            fileName = se.xpath("//*[@id='article-content']/div[%d]/div[2]/a/text()" % i).extract()
            item = WebcrawlerScrapyItem()
            item['name'] = fileName
            item['url'] = aurl
            print("*****NAME*****")
            print(fileName)
            print("*****NAME******")
            print("*****URL******")
            print(aurl)
            print("*****URL******")
            yield item

