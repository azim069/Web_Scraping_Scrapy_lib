import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class ReviewSpider(CrawlSpider):
    #name of the file and the link we get 
    name = "review"
    start_urls = ["https://www.trustpilot.com/categories/electronics_technology"]


    #Xpath rules for link 
    rules = (
            #For exracting the categories link
            Rule(LinkExtractor(restrict_xpaths='//div[@class="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2"]/a'), 
                  callback="parse_item", follow=True),
            #For the next page ,for getting company name and others things
            Rule(LinkExtractor(restrict_xpaths='//a[@aria-label="Next page"]'), 
                  callback="parse_item", follow=True),)
    
    #Method funtion,it's extract which type of data we wanna scrap
    def parse_item(self, response):
        item = {}
        Ratings = response.xpath('//span[@role="link"]/span/text()').get()
        yield{
            "Company" : response.xpath('//span[@class="typography_display-s__qOjh6 typography_appearance-default__AAY17 title_displayName__TtDDM"]/text()').get(),
            "Ratings" : Ratings.split()[]
        }
        return item

