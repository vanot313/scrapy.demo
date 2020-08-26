# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse


# 解决动态页面获取问题
class SeleniumMiddleware:
    def __init__(self, timeout=None, service_args=None, executable_path=None):
        if service_args is None:
            service_args = []
        self.timeout = timeout
        self.browser = webdriver.PhantomJS(executable_path=executable_path)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        self.browser.get(request.url)
        html = self.browser.page_source
        return HtmlResponse(url=request.url, body=html, request=request, encoding='utf-8')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'),
                   executable_path=crawler.settings.get('PHANTOMJS_EXECUTABLE_PATH')
                   )


# 解决ajax请求头访问问题
class RequestPlusMiddleware:

    def __init__(self, timeout=None):
        self.timeout = timeout

    def process_request(self, request, spider):
        response = spider.session.post(url=request.url, data=spider.formdata, headers=spider.headers)

        response.encoding = response.apparent_encoding
        html = response.content.decode('unicode-escape')

        return HtmlResponse(url=request.url, body=html, request=request, encoding='utf-8')
