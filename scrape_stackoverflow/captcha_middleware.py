from w3lib.http import basic_auth_header
from .spiders.config import API_KEY

class CustomProxyMiddleware(object):
    def process_request(self, request, spider):
            # request.meta['proxy'] = "&lt;http://proxy.scrapingdog.com:8081&gt;"
            request.headers['Proxy-Authorization'] = basic_auth_header('scrapingdog', API_KEY)