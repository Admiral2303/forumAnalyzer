# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import MessageItem
from .items import TitleItem

from .database.messageDB import ForumDatabase


class GrabberPipeline(object):

    def __init__(self):
        self.db = ForumDatabase()

    def process_item(self, item, spider):
        if isinstance(item, MessageItem):
            self.db.save_message(item.__dict__['_values'])
        if isinstance(item, TitleItem):
            self.db.save_title(item.__dict__['_values'])
        return item

    def close_spider(self, spider):
        self.db.close()
