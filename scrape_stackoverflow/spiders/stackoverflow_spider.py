from scrapy.loader import ItemLoader
from ..items import ScrapeStackoverflowItem
import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    page_number = 2
    def start_requests(self):
        yield scrapy.Request(f'https://stackoverflow.com/questions/tagged/{self.language}')

    def parse(self, response, **kwargs):
        details = response.css('#questions .s-link::attr(href)').extract()
        for url in details:
            yield scrapy.Request(response.urljoin(url), self.parse_detail)

        next_page = 'https://stackoverflow.com/questions/tagged/python?tab=newest&page=' + str(StackOverflowSpider.page_number) + '&pagesize=15'
        if StackOverflowSpider.page_number < 3:
            StackOverflowSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response):
        l = ItemLoader(ScrapeStackoverflowItem(), response)
        l.add_css('question', '#question-header .question-hyperlink')
        l.add_css('user_details_question', '#question .user-details a')
        l.add_css('detail_question', '#question .js-post-body p')
        print('QUESTION  CODE BLOCK')
        l.add_css('question_code_block', '#question .js-post-body code')
        l.add_css('verified_answer', '.js-accepted-answer p')
        l.add_css('verified_answer_code_block', '.js-accepted-answer .js-post-body code')
        l.add_css('verified_answer_user_details', '.js-accepted-answer .user-details a')
        l.add_css('answer', '.js-answer p')
        l.add_css('answer_code_block', '#answers .js-post-body code')
        l.add_css('answer_user_details', '#answers .user-details a')
        detail = "".join(l.load_item()['detail_question'])
        question_string = "".join(l.load_item()['question'])
        user_details_question_string = "".join(l.load_item()['user_details_question'])
        data = l.load_item()
        try:
            question_code_block_string = "".join(l.load_item()['question_code_block'])
            data['question_code_block'] = question_code_block_string
        except:
            data['question_code_block'] = "No Question Code Block"

        try:
            verified_answer_string = "".join(l.load_item()['verified_answer'])
            verified_answer_code_block_string = "".join(l.load_item()['verified_answer_code_block'])
            verified_answer_user_details_string = "".join(l.load_item()['verified_answer_user_details'])
            data['verified_answer'] = verified_answer_string
            data['verified_answer_code_block'] = verified_answer_code_block_string
            data['verified_answer_user_details'] = verified_answer_user_details_string

        except:
            data['verified_answer'] = "No Verified Answer Yet"
            data['verified_answer_code_block'] = "No Verified Answer Yet"
            data['verified_answer_user_details'] = "No Verified Answer Yet"

        try:
            answer_string = "".join(l.load_item()['answer'])
            answer_code_block_string = "".join(l.load_item()['answer_code_block'])
            answer_user_details_string = "".join(l.load_item()['answer_user_details'])
            data['answer'] = answer_string
            data['answer_code_block'] = answer_code_block_string
            data['answer_user_details'] = answer_user_details_string

        except:
            data['answer'] = "No Answer Yet"
            data['answer_code_block'] = "No Answer Yet"
            data['answer_user_details'] = "No Answer Yet"

        data['detail_question'] = detail
        data['question'] = question_string

        data['user_details_question'] = user_details_question_string
        print('DATA', data)
        yield data
