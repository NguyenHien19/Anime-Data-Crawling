# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    voting = scrapy.Field()
    duration = scrapy.Field()
    view = scrapy.Field()
    status = scrapy.Field()
    genre = scrapy.Field()
    director = scrapy.Field()
    country = scrapy.Field()
    follower = scrapy.Field()
    quality = scrapy.Field()
    rating = scrapy.Field()
    studio = scrapy.Field()
    season = scrapy.Field()

   
       