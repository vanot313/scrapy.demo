from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from webCrawler_scrapy.spiders import demo_spider
from webCrawler_scrapy.spiders.demo_spider import DemoSpider

# TODO APScheduler 自动化管理

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

# 创建一个CrawlerRunner对象
runner = CrawlerRunner()

d = runner.crawl(DemoSpider)  #