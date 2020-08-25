# -*- coding: utf-8 -*-


# TODO 爬虫名配置
BOT_NAME = 'demo_spider'  # 与自己实现的爬虫类中的name属性一致
SPIDER_MODULES = ['webCrawler_scrapy.spiders']
NEWSPIDER_MODULE = 'webCrawler_scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# TODO 配置下载器（自定义时装配）
DOWNLOADER_MIDDLEWARES = {
    # 'webCrawler_scrapy.middlewares.SeleniumMiddleware': 543,  # selenium解决动态页面
    'webCrawler_scrapy.middlewares.RequestPlusMiddleware': 543,  # request解决ajax post
}

# TODO 配置管道信息(自定义时装配)
ITEM_PIPELINES = {
    'webCrawler_scrapy.pipelines.WebcrawlerScrapyPipeline': 300,  # 保存到mysql数据库
    'webCrawler_scrapy.pipelines.JsonWithEncodingPipeline': 300,  # 保存到文件中
}

# TODO 配置Webdriver-PhantomJS与其他参数
PHANTOMJS_SERVICE_ARGS = []
SELENIUM_TIMEOUT = 20
# TODO 自行修改webdriver路径，这里采用phantomjs
PHANTOMJS_EXECUTABLE_PATH = r'C:\Tools\phantomjs-2.1.1-windows\bin\phantomjs.exe'

# Mysql数据库信息参数
# TODO 自行修改数据库配置
MYSQL_HOST = '101.132.131.184'
MYSQL_DBNAME = 'threat_info'  # 数据库名字，请修改
MYSQL_USER = 'root'  # 数据库账号，请修改
MYSQL_PASSWD = 'Ji1234'  # 数据库密码，请修改
MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'webCrawler_scrapy.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html


# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


