import scrapy
from anime.items import AnimeItem
import random

## Date crawl: 10-07-2023

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["animevietsub.moe"]

    # TV/Series
    # start_urls = ["https://animevietsub.moe/anime-bo/"]

    # Movie/OVA: 
    start_urls = ["https://animevietsub.moe/anime-le/"]

    custom_settings = {
        'FEED' : {
            #'anime_series.json' : {'format' : 'json', 'overwrite' : True},
            'anime_movie.json' : {'format' : 'json', 'overwrite' : True},
        }
    }

    def parse(self, response):
        for data in response.css('.TPostMv'):
            movie_url = data.css('article a::attr(href)').get()
            yield response.follow(movie_url, 
                                  callback=self.parse_movie_page)
            
        # Loop for tv/series: 123 pages
        """
        for i in range(1, 124):
            next_page_url = 'https://animevietsub.moe/anime-bo/trang-' + str(i) + '.html'
            yield response.follow(next_page_url, 
                                  callback=self.parse)
        """

        # Loop for movie/ova: 40 pages
        
        for i in range(1, 41):
            next_page_url = 'https://animevietsub.moe/anime-le/trang-' + str(i) + '.html'
            yield response.follow(next_page_url, 
                                  callback=self.parse)
        


    def parse_movie_page(self, response):
        item = AnimeItem()

        item['name'] = response.css('.Title::text').get() 
        item['description'] = response.css('.Description::text').get()
        item['voting'] = response.css('#TPVotes::attr(data-percent)').get() 
        item['duration'] = response.css('.Time.AAIco-access_time::text').get()
        item['view'] = response.css('.View.AAIco-remove_red_eye::text').get()

        if response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[2]/strong/text()').get() == 'Lịch chiếu:':
            item['status'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[3]/text()').get() 
            item['genre'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[4]/a/text()').getall()
            item['director'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[5]/a/text()').get()
            item['country'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[6]/a/text()').get()
            item['follower'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[7]/text()').get()
            
        elif response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[2]/strong/text()').get() == 'Trạng thái:':
            item['status'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[2]/text()').get() 
            item['genre'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[3]/a/text()').getall()
            item['director'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[4]/a/text()').get()
            item['country'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[5]/a/text()').get()
            item['follower'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[6]/text()').get()
        else:
            item['status'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[1]/text()').get() 
            item['genre'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[2]/a/text()').getall()
            item['director'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[3]/a/text()').get()
            item['country'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[4]/a/text()').get()
            item['follower'] = response.xpath('//*[@id="MvTb-Info"]/div[1]/ul/li[5]/text()').get()

        item['quality'] = response.css('.Qlty::text').get() 
        item['rating'] = response.css('.imdb::text').get() 
        item['studio'] =  response.xpath('//*[@id="MvTb-Info"]/div[2]/ul/li[5]/text()').get() 
        item['season'] = response.xpath('//*[@id="MvTb-Info"]/div[2]/ul/li[6]/a/text()').get()
        
        yield item


