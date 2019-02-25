# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WangyiPipeline(object):
    def process_item(self, item, spider):
        fp = open('C:\\Users\\李智坚\\Desktop\\py.file\\news.txt','a+')
        fp.write(item['time']+'\n')
        fp.write(item['title'] + '\n')
        fp.write(item['url'] + '\n')
        fp.write(item['content'] + '\n')
        return item
