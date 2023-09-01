#importing Lib
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class UclSpider(CrawlSpider):
    #name of data file
    name = "ucl"
    
    #The link we get 
    start_urls = ["https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century"]

    #Xpath rules
    rules = (
            #For exract book 
            Rule(LinkExtractor(restrict_xpaths='//tr/td/a'),
                   callback="parse_item", follow=True),
            #For The next page
            Rule(LinkExtractor(restrict_xpaths='//div[@class="pagination"]/a[@class="next_page"]')),
            )
    
    
    #metthod function ,which type of data we wanna scrap 
    def parse_item(self, response):
        
        #want to split the rating ,and take them out side of the yield.
        Five_Star = response.xpath('..//div[@data-testid="ratingBar-5"]/div[@class="RatingsHistogram__labelTotal"]/text()').get()
        Four_Star = response.xpath('..//div[@data-testid="ratingBar-4"]/div[@class="RatingsHistogram__labelTotal"]/text()').get()
        Three_star = response.xpath('..//div[@data-testid="ratingBar-3"]/div[@class="RatingsHistogram__labelTotal"]/text()').get()
        Two_star = response.xpath('..//div[@data-testid="ratingBar-2"]/div[@class="RatingsHistogram__labelTotal"]/text()').get()
        One_star = response.xpath('//div[@data-testid="ratingBar-1"]/div[@class="RatingsHistogram__labelTotal"]/text()').get()

        yield{
            "Book_Name" : response.xpath('..//div/h1/text()').get(),
            "Author"    : response.xpath('..//span[@tabindex="-1"]/a/span[@class="ContributorLink__name"]/text()').get(),
            "Average_star"   : response.xpath('..//a/div/div[@class="RatingStatistics__rating"]/text()').get(),
            "Ratings"  : response.xpath('..//div/div/div/span[@data-testid="ratingsCount"]/text()')[0].get(),
            "Reviews"  : response.xpath('..//div/div/div/span[@data-testid="reviewsCount"]/text()')[0].get() ,
            #Spliting with the "split()"
            "5_Star": Five_Star.split()[0],
            "4_Star": Four_Star.split()[0],
            "3_Star": Three_star.split()[0],
            "2_Star": Two_star.split()[0],
            "1_Star": One_star.split()[0]
            

        }
    
