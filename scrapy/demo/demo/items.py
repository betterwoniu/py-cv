# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DouBanItem(scrapy.Item):
   rating = scrapy.Field()
   quote = scrapy.Field()
   title = scrapy.Field()
