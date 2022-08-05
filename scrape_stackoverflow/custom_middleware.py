class CustomProxyMiddleware(object):

    def process_request(self, request, spider):
        print('PROXY================================================================================================')
        # request.meta["proxy"] = "https://157.100.12.138:999"
        request.meta['proxy'] = "https://102.68.128.212:8080"
        # request.meta['proxy'] = "https://102.68.135.129:8080"
        # request.meta["proxy"] = "https://204.199.174.75:999"
        # request.meta["proxy"] = "https://95.111.243.221:5566"
        # request.meta["proxy"] = "https://183.89.168.192:8080"
        print(request.meta, 'heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

