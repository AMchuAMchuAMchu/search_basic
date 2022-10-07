import scrapy
from items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijut.cc']
    start_urls = ['http://meijut.cc/label/news.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list fn-clear"]/li')
        print('========')
        print('========')
        print('========')
        print(movies)
        print('========')
        print('========')
        print('========')
        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item
