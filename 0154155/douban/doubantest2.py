import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
if __name__ == '__main__':
    url = 'https://book.douban.com/top250?start=25'
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('tr[@class = "item"]')
    for info in infos:
        names = selector.xpath('td/div/a/@title')
        for name in names:
            print(name)
