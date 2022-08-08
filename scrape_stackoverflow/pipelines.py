# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from configparser import ConfigParser

from django.conf import settings
from itemadapter import ItemAdapter
import psycopg2
import pymongo
from scrapy.exceptions import DropItem
from scrapy_proxies.randomproxy import log

from .items import ScrapeStackoverflowItem


class ScrapeStackoverflowPipeline:

    def __init__(self):
        connection = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = connection["stackoverflow"]
        self.collection = db["questions"]

    # def __init__(self):
    #     print("INSIDE INIT")
    #     self.configg = ConfigParser()
    #     self.configg.read('configuration.ini')
    #
    #     self.user = (self.configg['database']['user'])
    #     self.password = self.configg['database']['password']
    #     self.host = self.configg['database']['host']
    #     self.port = self.configg['database']['port']
    #     self.database = self.configg['database']['database']
    #     print(self.user, 'user')
    #     print(self.database, 'DATABASES')
    #     print(self.password, 'password')
    #     print(self.host, 'host')
    #
    #     self.conn = psycopg2.connect(user=self.user,
    #                                  password=self.password,
    #                                  host=self.host,
    #                                  port=self.port,
    #                                  database=self.database)
    #     self.cur = self.conn.cursor()
    #     self.create_table()
    #
    # def create_table(self):
    #     print('INSIDE CREATE TABLE')
    #     self.cur.execute("""CREATE TABLE IF NOT EXISTS stackoverflow_data(
    #             id SERIAL PRIMARY KEY,
    #             question TEXT,
    #             user_details_question TEXT,
    #             detail_question TEXT,
    #             code_block TEXT,
    #             verified_answer TEXT,
    #             user_details_answer TEXT)
    #     """)

    def process_item(self, item, spider):
        item['code_block'] = str(item['code_block'])
        print(item['code_block'], '11111111111111111111111111111111111111111111111111111111111111111111111111')
        print(str(item['code_block']), '2222222222222222222222222222222222222222222222222222222222222222222222')
        # data = dict(ScrapeStackoverflowItem(item))
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            print(dict(item), 'DICT ITEMS------------------------------------------------')
            # print(data, 'DATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            self.collection.insert_one(dict(item))
            logging.info("Question added to MongoDB database!")
        return item