# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from configparser import ConfigParser

from itemadapter import ItemAdapter
import psycopg2


class ScrapeStackoverflowPipeline:

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
        # print(item['question'], 'CODEDEEEEEEEEEEEEEEEEEEE')
        # print(item['verified_answer'][0], 'ANSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
        # print(item, 'ITEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEMMMMMMMMMM')
        # print('PIPELINESS', item['verified_answer'][0].strip('<p>,</p>'))
        # print('PIPELINES DETAIL QUESTION', item['detail_question'])
        return item