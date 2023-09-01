import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ReviewSpider(CrawlSpider):
    #name of the file and the link we get 
    name = "review"
    start_urls = ["https://www.trustpilot.com/categories/electronics_technology"]


    #Xpath rules for link 
    rules = (
            #For exracting the categories link
            Rule(LinkExtractor(restrict_xpaths='//div[@class="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2"]/a), 
                  callback="parse_item", follow=True),
            #For the next page ,for getting company name and others things
            Rule(LinkExtractor(restrict_xpaths=""), 
                  callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
