from random import random

from scrapy.loader import ItemLoader

from ..items import ScrapeStackoverflowItem
import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    page_number = 2
    start_urls = [
        'https://stackoverflow.com/questions/73233110/why-the-scatter-plot-is-plotting-zero-data-points-when-the-data-has-no-zero-valu',
    ]

    def start_requests(self):
        yield scrapy.Request(f'https://stackoverflow.com/questions/tagged/{self.language}')




    # CUSTOM_PROXY = "http://94.51.83.2:8080"
    #
    # def start_requests(self):
    #     for url in self.start_urls:
    #         request = scrapy.Request(url, callback=self.parse)
    #         request.meta['proxy'] = self.CUSTOM_PROXY
    #         yield request

    def parse(self, response):
        print('YYAAAYYYY')
        print(response, 'RESPONSE DATA---------------===========================================================')
        details = response.css('#questions .s-link::attr(href)').extract_first()
        print(details, '*******************************************************************************')
        yield (scrapy.Request(response.urljoin(details), self.parse_detail))




        # next_page = 'https://stackoverflow.com/questions/tagged/python?tab=newest&page=' +
        # str(StackOverflowSpider.page_number) + '&pagesize=15'
        # if StackOverflowSpider.page_number<133250:
        #     StackOverflowSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)

        # for url in details:
        #     print(url, 'url----------------------------------------------------------------------------------------')
        #     yield (scrapy.Request(response.urljoin(url), self.parse_detail))

    def parse_detail(self, response):
        l = ItemLoader(ScrapeStackoverflowItem(), response)
        l.add_css('question', '#question-header .question-hyperlink')
        l.add_css('user_details_question', '#question .user-details a')
        l.add_css('detail_question', '#question .js-post-body p')
        l.add_xpath('code_block', '//*[@id="question"]/div[2]/div[2]/div[1]/pre/code')
        l.add_css('verified_answer', '.js-accepted-answer p')
        l.add_css('user_details_answer', '.js-accepted-answer .user-details a')
        print('LOAD ITEMMMMM', l.load_item())
        detail = "".join(l.load_item()['detail_question'])
        data = l.load_item()
        data['detail_question'] = detail
        print('DATA', data)
        yield data
