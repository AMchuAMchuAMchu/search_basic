# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviePipeline(object):
    def process_item(self, item, spider):
        with open(file="d:/my_meiju.txt",encoding='utf-8',mode='a') as fp:
            print(type(item['name']))
            fp.write(item['name'] + "\n")
