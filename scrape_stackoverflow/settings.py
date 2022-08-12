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


PROXY_MODE = 0

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_IP = 3

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrape_stackoverflow.pipelines.ScrapeStackoverflowPipeline': 300,
}
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "stackoverflow"
MONGODB_COLLECTION = "questions"