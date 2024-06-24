# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CcsbaseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class CcsItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    adduct = scrapy.Field()
    mass =  scrapy.Field()
    ccs = scrapy.Field()
    smile = scrapy.Field()
    charge = scrapy.Field()    