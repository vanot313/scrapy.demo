# coding=utf-8
import json
import requests
import scrapy
from webCrawler_scrapy import settings
from scrapy import FormRequest
from webCrawler_scrapy.items import \
    WebcrawlerScrapyItem  # 导入item对应的类，crawlPictures是项目名，items是items.py文件，import的是items.py中的class，也可以import *
from webCrawler_scrapy.util.tools import getToken


class DemoSpider(scrapy.spiders.Spider):
    # TODO 自定义爬虫名，要和settings中的BOT_NAME属性对应的值一致
    name = "demo_spider"

    # TODO 网页爬取起始位置与网页爬取范围
    allowed_domains = ["https://nosec.org"]  # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    # start_urls = ["https://nosec.org/home/index/security.html/"]  # 开始爬取的地址

    # 建立一次会话获取token,配置请求头,请求参数
    session = requests.session()
    token = getToken(session)
    headers = {
        'User-Agent': settings.USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'X-Requested-With': "XMLHttpRequest",
        'X-CSRF-TOKEN': str(token)
    }
    formdata = {}

    # 逐页爬取
    def start_requests(self):
        url = 'https://nosec.org/home/ajaxindexdata'
        for i in range(1, 3):
            self.formdata = {
                'page': str(i),
                'keykind': 'security',
            }

            request = FormRequest(url, callback=self.parse, formdata=self.formdata, headers=self.headers)
            yield request

    # TODO 处理爬虫数据逻辑
    def parse(self, response):
        # 获取返回json数据
        data = str(response.body.decode("utf-8"))
        # 处理json字串中特殊的错误：解决末尾单独“问题
        data = data.replace('"...', '...')

        res = json.loads(data)["data"]["threatData"]["data"]
        for it in res:
            id = it["id"].replace("'", "\\'")
            title = it["title"].replace("'", "\\'")

            item = WebcrawlerScrapyItem()
            item['t_name'] = title
            item['t_url'] = "https://nosec.org/home/detail/" + id + ".html"

            yield item
