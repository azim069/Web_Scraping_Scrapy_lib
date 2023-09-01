import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ReviewSpider(CrawlSpider):
    name = "review"
    start_urls = ["https://www.trustpilot.com/"]


    #
    rules = (Rule(LinkExtractor(restrict_xpaths=""), 
                  callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
