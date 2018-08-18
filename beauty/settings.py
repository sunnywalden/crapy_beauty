# -*- coding: utf-8 -*-

# Scrapy settings for beauty project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'beauty'

SPIDER_MODULES = ['beauty.spiders']
NEWSPIDER_MODULE = 'beauty.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_REQUESTS_PER_IP = 32

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'beauty.middlewares.BeautySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_proxies.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#    'beauty.middlewares.BeautyDownloaderMiddleware': 543,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':None,
#    'beauty.middlewares.BeautySpiderMiddleware':125,
#    'beauty.middlewares.ProxyMiddleWare':125,
#    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'beauty.pipelines.ImgDownloadPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IMAGES_STORE = '/Users/cloudin/Documents/images/beauty'
IMAGES_EXPIRES = 30
LOG_FILE = "./logs/beauty.log"
LOG_ENCODING = "UTF-8"
LOG_ENABLED = True
LOG_LEVEL = "INFO"
DOWNLOAD_FAIL_ON_DATALOSS = False
DOWNLOAD_TIMEOUT = 15
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#RETRY_HTTP_CODECS = "500,502,503,504,408"
PROXY_LIST = '/tmp/proxies_beauty.txt'
PROXY_MODE = 0

IPPOOL=[
	{"ipaddr":"167.99.153.166:8080"},
	{"ipaddr":"151.106.52.123:1080"},
	{"ipaddr":"142.4.209.32:3128"},  
	{"ipaddr":"95.211.242.43:808"},
	{"ipaddr":"181.199.199.247:53281"},
	{"ipaddr":"167.99.197.73:8080"},
	{"ipaddr":"151.106.52.243:1080"},
	{"ipaddr":"140.143.105.245:80"},
	{"ipaddr":"39.104.59.236:8080"},
	{"ipaddr":"124.238.248.4:80"}
]

IMAGES_THUMBS = {
#    'small': (50, 50),
    'big': (270, 270),
}
