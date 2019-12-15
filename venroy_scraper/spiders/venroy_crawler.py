# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule	
from venroy_scraper.items import VenroyScraperItem, ProductLoader
from pprint import pprint


class VenroyCrawlerSpider(CrawlSpider):
    name = 'venroy_crawler'
    allowed_domains = ['venroy.com.au']
    start_urls = ['http://venroy.com.au/']
    rules = (Rule(LinkExtractor(allow='collections/', deny=('spring-18-mens', 'spring-18' , 'gift-cards', 'shop-all-mens', 'shop-all-womens', 'shop-new-womens')), callback='parse_categories', follow=True),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="grid-view-item__link grid-view-item__image-container"]',)), callback='parse_product'),
    )


    def parse_categories(self, response):
        item = {}
        pprint('Got a response from %s.' % response.url)
        return item


    def parse_product(self, response):
        loader = ProductLoader(selector=response)
        loader.add_xpath('product_name', '//h1[@class="product-single__title"]/text()')
        loader.add_xpath('colour', '//div[@class="colors"]/a/@alt')
        loader.add_xpath('price', '//span[@id="ProductPrice-product-template"]/text()')
        loader.add_xpath('image_urls', '//img[@class="desktop-zoom"]/@src')
        loader.add_xpath('description', '//div[@class="product-single__description rte"]/p/span/text()')
        return loader.load_item()

