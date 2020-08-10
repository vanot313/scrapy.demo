# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse


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
        """
        用PhantomJS抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        self.browser.get(request.url)
        html = self.browser.page_source
        return HtmlResponse(url=request.url, body=html, request=request, encoding='utf-8')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'),
                   executable_path=crawler.settings.get('PHANTOMJS_EXECUTABLE_PATH')
                   )
