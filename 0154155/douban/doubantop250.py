import requests
from lxml import etree
import csv


fp = open('C:\\Users\\李智坚\\Desktop\\py.file\\doubanbook.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('name', 'url', 'author', 'publisher', 'publish_data', 'price', 'rate', 'comment'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

urls =[ 'https://book.douban.com/top250?start={}'.format(str(i))  for i in range(0, 250, 25)]
for url in urls:

    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class = "item"]')

    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        p_url = info.xpath('td/div/a/@href')[0]
        bookinfo = info.xpath('td/p/text()')[0]
        author = bookinfo.split('/')[0]
        publisher = bookinfo.split('/')[-3]
        publish_data = bookinfo.split('/')[-2]
        price = bookinfo.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')
        comment = info.xpath('td/p/span/text()')
        writer.writerow((name, p_url, author, publisher, publish_data, price, rate, comment))


fp.close()
