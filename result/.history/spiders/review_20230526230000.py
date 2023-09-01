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
            Company = response.xpath('//span[@class="typography_display-s__qOjh6 typography_appearance-default__AAY17 title_displayName__TtDDM"]/text()').get()
        except:
            Company = 'None'
        try:
            Total_Reviews = response.xpath('//span[@class="typography_body-l__KUYFJ typography_appearance-subtle__8_H2l styles_text__W4hWi"]/text()[1]').get()
        except:
            Total_Reviews ='None'
        try:    
            Scale = response.xpath('//span[@class="typography_body-l__KUYFJ typography_appearance-subtle__8_H2l styles_text__W4hWi"]/text()[5]').get()
        except:
            Scale = 'None'
        try:
            Ratings = response.xpath('//span[@class="typography_heading-m__T_L_X typography_appearance-default__AAY17"]/text()').get()
        except:
            Ratings = 'None'
        try:
            Five_star = response.xpath('//p[@class="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_percentageCell__cHAnb"]/text()[1]').get()
        except:
            Five_star = 'None'
        try:
            Four_star = response.xpath('//p[@class="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_percentageCell__cHAnb"]/text()[2]').get()
        except:
            None
        try:
            Three_star = response.xpath('//p[@class="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_percentageCell__cHAnb"]/text()[3]').get()
        except:
            None
        try:
            Two_star = response.xpath('//p[@class="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_percentageCell__cHAnb"]/text()[4]').get()
        except:
            None
        try:
            One_star = response.xpath('//p[@class="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_percentageCell__cHAnb"]/text()[5]').get()
        except:
            None	


        yield{
            "Company"               : Company,
            "Total Reviews"         : Total_Reviews,
            "Scale"                 : Scale,
            "Ratings"               : Ratings,
            "1-star"                : One_star,
            "2-star"                : Two_star,
            "3-star"                : Three_star,
            "4-star"                : Four_star,
            "5-star"                : Five_star
 
        }
        return item

