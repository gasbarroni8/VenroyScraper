# Web Scraping and Crawling with Scrapy

> Created a CrawlSpider to extract products from https://venroy.com.au/


To run a crawler run this next command from the root directory of a project:
```
scrapy crawl venroy_crawler
```

Creates a csv file with crawled data. Includes following fields:
* product_name
* colour (if multiple - splitted by ;)
* price
* image_urls (splitted by ;)
* description
