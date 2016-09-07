# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class PythonjobsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()
    city = Field()
    company = Field()
    location = Field()
    description = Field()
    salary_lower = Field()
    salary_upper = Field()