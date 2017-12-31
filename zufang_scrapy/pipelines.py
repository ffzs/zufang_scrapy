# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ZufangScrapyPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient("mongodb://ffzs:lj910226@192.168.3.7:2018",connect=False)
        db = client["test"]
        self.collection = db["zufang-beijing"]

    def process_item(self, item, spider):
        content = dict(item)
        self.collection.insert(content)
        print("###################已经存入MongoDB########################")
        return item

    def close_spider(self, spider):
        pass
