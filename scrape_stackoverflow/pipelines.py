# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import pymongo
from scrapy.exceptions import DropItem


class ScrapeStackoverflowPipeline:

    def __init__(self):
        connection = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = connection["stackoverflow"]
        self.collection = db["questions"]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert_one(dict(item))
            logging.info("Question added to MongoDB database!")
        return item