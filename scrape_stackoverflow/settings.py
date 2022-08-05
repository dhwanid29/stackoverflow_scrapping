# Scrapy settings for scrape_stackoverflow project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrape_stackoverflow'

SPIDER_MODULES = ['scrape_stackoverflow.spiders']
NEWSPIDER_MODULE = 'scrape_stackoverflow.spiders'

# ROBOTSTXT_OBEY = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_stackoverflow (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
PROXY_POOL_ENABLED = True
# PROXY_POOL_FILTER_CODE = 'IN'
# DOWNLOAD_DELAY = 0.15


ROTATING_PROXY_LIST = [
    '124.158.167.18:8080',
    '198.59.191.234:8080',
]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_proxies.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
PROXY_LIST = 'scrape_stackoverflow/list.txt'
RANDOM_UA_PER_PROXY = True

DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 100,
    # 'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 100,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 190,
    'scrapy_proxies.RandomProxy': 110,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
#CUSTOM_PROXY = "http://host1:port"


# DOWNLOADER_MIDDLEWARES = {
#     # 'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     # 'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
#     # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     # 'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#     #     'rotating_proxies.middlewares.RotatingProxyMiddleware': 200,
#     #     'rotating_proxies.middlewares.BanDetectionMiddleware': 200,
#     #     # 'scrape_stackoverflow.policy.MyPolicy': 350,
#     'scrape_stackoverflow.custom_middleware.CustomProxyMiddleware': 110,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
# }
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    # 'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    #


# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
# PROXY_POOL_BAN_POLICY = 'scrape_stackoverflow.policy.MyPolicy'


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_IP = 3
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrape_stackoverflow.middlewares.ScrapeStackoverflowSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrape_stackoverflow.middlewares.ScrapeStackoverflowDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrape_stackoverflow.pipelines.ScrapeStackoverflowPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# ROTATING_PROXY_LIST = [
#     '157.100.12.138:999',
#     '200.25.254.193:54240',
#     '204.199.174.75:999',
#     '183.89.168.192:8080',
#     '181.118.158.133:999',
#     '95.111.243.221:5566',
#     '161.22.35.62:999',
#     '181.78.64.39:999',
#     '189.157.132.229:999',

    # '103.97.46.214:83',
    # '201.184.107.26:999',
    # '50.114.111.97:3128',
    # '12.88.29.66:9080',
    # '181.49.212.122:5678',
    # '95.142.223.24:56379',
    # '185.93.32.166:3128',
    # '178.151.205.154:45099',
    # '118.174.142.242:8080',
    # '204.199.174.75:999',
    # '195.222.107.85:4153',
    # '3.68.76.43:9999',
    # '41.65.227.166:1981',
    # '168.181.196.76:8080',
    # '50.227.121.37:80',
    # '82.165.184.53:80',
    # '49.48.49.211:8080',
    # '85.187.195.137:8080',
    # '94.75.76.3:8080',
    # '200.111.182.6:443',
    # '75.119.203.237:3540',
    # '185.51.10.19:80',
    # '181.129.138.114:30838',
    # '118.174.91.120:4145',
    # '125.25.49.121:8080',
    # '103.48.68.34:83',
    # '1.4.195.114:4145',
    # '204.199.174.74:999',
    # '138.59.187.33:666',
    # '195.12.14.4:8080',
    # '103.207.8.130:23804',
    # '62.201.220.50:60212',
    # '45.5.57.118:8080',
    # '47.57.188.208:80',
    # '216.250.156.85:80',
    # '157.119.211.133:8080',
    # '13.115.164.21:24432',
    # '178.238.25.174:1337',
    # '51.15.8.75:3738',
    # '176.62.178.247:47556',
    # '190.103.28.197:999',
    # '201.71.2.41:999',
    # '130.41.47.235:8080',
    # '77.233.5.68:55443',
    # '125.25.32.141:8080',
    # '51.75.206.209:80',
    # '182.160.127.53:48744',
    # '78.30.230.117:50932',
    # '170.83.79.226:999',
    # '185.15.172.212:3128',
    # '194.146.110.228:1080',
    # '93.116.11.12:3128',
    # '168.138.211.5:8080',
    # '147.135.134.57:9300',
    # '178.54.21.203:8081',
    # '50.114.110.113:3128',
    # '103.138.5.100:4145',
    # '204.199.174.72:999',
    # '62.193.108.149:1976',
    # '103.66.196.218:23500',
    # '112.78.170.29:2580',
    # '97.74.92.60:80',
    # '51.195.81.233:8080',
    # '156.239.50.167:3128',
    # '185.200.38.235:10820',
    # '83.238.80.2:8081',
    # '185.70.218.13:42707',
    # '5.202.191.226:80',
    # '103.150.218.46:1080',
    # '223.29.199.144:55443',
    # '179.48.150.190:888',
    # '197.232.135.174:41890',
    # '84.22.61.69:1080',
    # '211.142.96.250:9091',
    # '103.121.41.165:8080',
    # '154.202.101.63:3128',
    # '41.65.251.84:1981',
    # '167.172.178.193:34969',
    # '151.22.181.215:8080',
    # '154.236.168.179:1976',
    # '222.124.193.113:8080',
    # '94.130.244.179:5566',
    # '103.75.185.134:6359',
    # '46.98.251.182:8081',
    # '41.65.236.57:1976',
    # '45.189.113.111:999',
    # '45.225.184.145:999',
    # '193.233.137.216:8085',
    # '162.217.248.10:3128',
    # '189.203.234.146:999',
# ]

