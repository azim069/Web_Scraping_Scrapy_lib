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
        try:
            Company = response.xpath('//span[@class="typography_display-s__qOjh6 typography_appearance-default__AAY17 title_displayName__TtDDM"]/text()').get(),
        except:
            None
        try:
            Total_Reviews = response.xpath('//span[@class="typography_body-l__KUYFJ typography_appearance-subtle__8_H2l styles_text__W4hWi"]/text()[1]').get(),
        except:
            None
        try:    
            Scale = response.xpath('//span[@class="typography_body-l__KUYFJ typography_appearance-subtle__8_H2l styles_text__W4hWi"]/text()[5]').get()
        except:
            None
        try:
            Ratings = response.xpath('//span[@class="typography_heading-m__T_L_X typography_appearance-default__AAY17"]/text()').get()
        except:
            None
        try:
            Five_star = llll
        except:
            None
        try:
            Four_star = llll
        except:
            None
        try:
            Three_star = llll
        except:
            None
        try:
            Two_star = llll
        except:
            None
        try:
            One_star = llll
        except:
            None	




        yield{
            "Company"               : Company,
            "Total Reviews"         : Total_Reviews,
            "Scale"                 : Scale,
            "Ratings"               : Ratings,
            "1-star"              : ,
            "2-star"              : ,
            "3-star"                :
 
        }
        return item

