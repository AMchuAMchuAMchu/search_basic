# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviePipeline(object):
    def process_item(self, item, spider):
        with open(file='d:/demo/my_meiju.txt',mode='w') as fp:
            fp.write(item['name'].encode('utf-8')+'\n')