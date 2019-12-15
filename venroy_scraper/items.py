# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst
from scrapy.loader import ItemLoader
import re

class VenroyScraperItem(scrapy.Item):
    product_name = scrapy.Field()
    colour = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    description = scrapy.Field()


def extract_price(price_str):
    return re.search('[0-9.]+', price_str).group() 


class ProductLoader(ItemLoader):
    default_item_class = VenroyScraperItem
    product_name_out = TakeFirst()
    colour_out = Compose(MapCompose(lambda v: v.strip()), Join('; '))
    price_out = Compose(TakeFirst(), extract_price)
    image_urls_out = Compose(MapCompose(lambda v: v.strip()), Join('; '))
    description_out = Compose(MapCompose(lambda v: v.strip()), Join())
