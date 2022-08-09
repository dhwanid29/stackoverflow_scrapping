from random import random

from scrapy.loader import ItemLoader

from ..items import ScrapeStackoverflowItem
import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    page_number = 2
    start_urls = [
        # 'https://stackoverflow.com/questions/47105138/how-to-convert-an-array-to-string-efficiently-in-pyspark-python',
        # 'https://stackoverflow.com/questions/44135225/attributeerror-logger-object-has-no-attribute-warning',
        'https://stackoverflow.com/questions/11624190/how-to-convert-string-to-byte-array-in-python',
    ]
    #
    # def start_requests(self):
    #     yield scrapy.Request(f'https://stackoverflow.com/questions/tagged/{self.language}')


    def parse(self, response):
        print(response, 'RESPONSE DATA---------------===========================================================')
        details = response.css('#questions .s-link::attr(href)').extract_first()
        # for url in details:
        #     print(url, 'url----------------------------------------------------------------------------------------')
        #     yield (scrapy.Request(response.urljoin(url), self.parse_detail))
        # print(details, '*******************************************************************************')
        yield (scrapy.Request(response.urljoin(details), self.parse_detail))

        # next_page = 'https://stackoverflow.com/questions/tagged/python?tab=newest&page=' + str(StackOverflowSpider.page_number) + '&pagesize=15'
        # if StackOverflowSpider.page_number < 3:
        #     StackOverflowSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)



    def parse_detail(self, response):
        l = ItemLoader(ScrapeStackoverflowItem(), response)
        l.add_css('question', '#question-header .question-hyperlink')
        l.add_css('user_details_question', '#question .user-details a')
        l.add_css('detail_question', '#question .js-post-body p')
        l.add_css('code_block', '#question .js-post-body code')
        l.add_css('verified_answer', '.js-accepted-answer p')
        l.add_css('verified_answer_code_block', '.js-accepted-answer .js-post-body code')
        l.add_css('user_details_answer', '.js-accepted-answer .user-details a')
        print('LOAD ITEMMMMM', l.load_item())
        detail = "".join(l.load_item()['detail_question'])
        question_string = "".join(l.load_item()['question'])
        user_details_question_string = "".join(l.load_item()['user_details_question'])
        code_block_string = "".join(l.load_item()['code_block'])
        verified_answer_string = "".join(l.load_item()['verified_answer'])
        user_details_answer_string = "".join(l.load_item()['user_details_answer'])
        verified_answer_code_block_string = "".join(l.load_item()['verified_answer_code_block'])
        data = l.load_item()
        print(data, 'DATA')
        try:
            if not data['verified_answer']:
                pass
        except:
            l.add_css('answer', '.js-answer')
            l.add_css('answer_code_block', '.language-python')

        data['detail_question'] = detail
        data['question'] = question_string
        data['verified_answer'] = verified_answer_string
        data['verified_answer_code_block'] = verified_answer_code_block_string
        data['code_block'] = code_block_string
        data['user_details_answer'] = user_details_answer_string
        data['user_details_question'] = user_details_question_string
        print('DATA', data)
        yield data
