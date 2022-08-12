# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class ScrapeStackoverflowItem(scrapy.Item):
    question = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    detail_question = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    question_code_block = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    user_details_question = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    verified_answer = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    verified_answer_user_details = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    verified_answer_code_block = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    answer = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    answer_user_details = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
    answer_code_block = scrapy.Field(input_processor=MapCompose(remove_tags), output_processors=TakeFirst())
