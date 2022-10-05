import scrapy

from items import MovieItem
import lxml


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijut.cc']
    start_urls = ['http://meijut.cc/label/news.html']

    def parse(self, response):
        print(888888888)  # 测试用
        print()
        print()
        print()

        movies = response.xpath(
            '//ul[@class="top-list[\\s\\s\\s]fn-clear"]/li')  # 意思是选中所有的属性class值为"top-list  fn-clear"的ul下的li标签内容

        print(movies)  # 测试用

        print()
        print()
        print()

        for each_movie in movies:
            item = MovieItem()

            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]

            # .表示选取当前节点，也就是对每一项li，其下的h5下的a标签中title的属性值

            yield item  # 一种特殊的循环
