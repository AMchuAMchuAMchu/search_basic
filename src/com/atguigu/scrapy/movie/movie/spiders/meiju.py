import sys

import scrapy

# from movie.items import MovieItem
sys.path.append('../../')
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['www.meiju56.com']
    start_urls = ['http://www.meiju56.com/']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list fn-clear"]/li')
        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item




