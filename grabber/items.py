# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class MessageItem(Item):
    text = Field()
    author = Field()
    date = Field()
    title_name = Field()


class TitleItem(Item):
    name = Field()
    page_count = Field()
    url = Field()
