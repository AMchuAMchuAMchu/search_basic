import scrapy
from items import MovieItem
class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijut.cc']
    start_urls = ['http://meijut.cc/label/news.html']

    def parse(self, response):
        count = 0
        movies = response.xpath('//ul[@class="top-list fn-clear"]/li')
        # print(movies.extract())
        for each_movie in movies:
            count += 1
            # item = MovieItem()
            # item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            res = each_movie.xpath('./h5/a/@title').extract()[0]
            print(count,'>>',res)
            # file = open(file=r'D:\seldom\rd\Python_ProjectAll\search_basic\src\com\atguigu\scrapy\movie\meiju.txt',mode='w',encoding='utf-8')
            # res02 = str(count)+'>>'+res
            # file.writelines(str(res02))
            # yield item

