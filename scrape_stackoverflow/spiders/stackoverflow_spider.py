from scrapy.loader import ItemLoader
from scrape_stackoverflow.items import ScrapeStackoverflowItem
import scrapy
import logging


class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    page_number = 2

    # start_urls = ['https://stackoverflow.com/questions/67922817/xslt-2-0-group-adjacent-based-on-attribute-value']

    def start_requests(self):
        logging.info("Start Request URL")
        yield scrapy.Request(f'https://stackoverflow.com/search?q={self.search}')

    def parse(self, response, **kwargs):
        logging.info("Get question from search parameter")
        details = response.css('#questions .s-link::attr(href)').extract()
        # yield scrapy.Request(response.urljoin(details), self.parse_detail)
        for url in details:
            yield scrapy.Request(response.urljoin(url), self.parse_detail)

        # next_page = 'https://stackoverflow.com/questions/tagged/python?tab=newest&page=' + str(StackOverflowSpider.page_number) + '&pagesize=15'
        # if StackOverflowSpider.page_number < 2:
        #     StackOverflowSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response):
        logging.info("Load Question Details from each question link.")
        l = ItemLoader(ScrapeStackoverflowItem(), response)
        l.add_css('question', '#question-header .question-hyperlink')
        l.add_css('user_details_question', '#question .user-details a')
        l.add_css('detail_question', '#question .js-post-body p')
        l.add_css('question_code_block', '#question .js-post-body code')
        l.add_css('verified_answer', '.js-accepted-answer p')
        l.add_css('verified_answer_code_block', '.js-accepted-answer .js-post-body code')
        l.add_css('verified_answer_user_details', '.js-accepted-answer .user-details a')
        l.add_css('answer', '.js-answer p')
        l.add_css('answer_code_block', '#answers .js-post-body code')
        l.add_css('answer_user_details', '#answers .user-details a')
        data = l.load_item()
        data = data.deepcopy()

        for key, value in data.items():
            value_string = "".join(l.load_item()[key])
            data[key] = value_string

        if 'verified_answer' in data:
            data['answer'] = "No answer"
            data['answer_code_block'] = "No answer code block"
            data['answer_user_details'] = "No answer answer user details"
        elif 'answer' in data:
            data['verified_answer'] = "No verified answer"
            data['verified_answer_code_block'] = "No verified answer code block"
            data['verified_answer_user_details'] = "No verified answer answer user details"
        elif 'verified_answer' not in data.keys() and 'answer' not in data:
            data['verified_answer'] = "No verified answer"
            data['verified_answer_code_block'] = "No verified answer code block"
            data['verified_answer_user_details'] = "No verified answer answer_user_details"
            data['answer'] = "No answer"
            data['answer_code_block'] = "No answer code block"
            data['answer_user_details'] = "No answer answer user details"
        yield data
