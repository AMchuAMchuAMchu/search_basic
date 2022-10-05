import scrapy

from items import MovieItem
from lxml import etree


class MeijuSpider(scrapy.Spider):
    # 爬虫名
    name = 'meiju'
    # 被允许的域名
    allowed_domains = ['meijut.cc']
    # 起始爬取的url
    start_urls = ['http://meijut.cc/label/news.html']

    # 数据处理
    def parse(self, response):
        # response响应对象
        # xpath
        mytree = etree.HTML(response.text)
        movie_list = mytree.xpath('//ul[@class="top-list  fn-clear"]/li')
        print(movie_list)

        for movie in movie_list:
            name = movie.xpath('./h5/a/text()')

            # 创建item(类字典对象)
            item = MovieItem()
            item['name'] = name
            yield item