from scrapy_proxy_pool.policy import BanDetectionPolicy


class MyPolicy(BanDetectionPolicy):
    def response_is_ban(self, request, response):
        print('INSIE BANNNN')
        request.meta['proxy'] = "https://102.68.128.212:8080"
        # use default rules, but also consider HTTP 200 responses
        # a ban if there is 'captcha' word in response body.
        # print(f"RESPONSE: {response.body}")
        # ban = super(MyPolicy, self).response_is_ban(request, response)
        # ban = ban or b'captcha' in response.body
        return True

    def exception_is_ban(self, request, exception):
        # override method completely: don't take exceptions in account
        return None