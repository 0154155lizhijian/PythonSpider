import re

import requests
from lxml import etree
from bs4 import BeautifulSoup


# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# }
#
# def get_news_url(url):
#     res = requests.get(url, headers=headers)
#     selector = etree.HTML(res.text)
#     news_herfs = selector.xpath('//div/div/ul/li/strong/a/@href')
#     for news_herf in news_herfs:
#         get_news_info(news_herf)
# def get_news_info(url):
#     res = requests.get(url,headers =headers)
#     soup = BeautifulSoup(res.content,'lxml')
#     print(soup)
#
# if __name__ == '__main__':
#     url = 'https://news.baidu.com/'
#     get_news_url(url)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url = 'http://new.qq.com/'
res = requests.get(url,headers = headers)
soup = BeautifulSoup(res.text,'lxml')
print(soup)
# content = re.findall('<p class="one-p">(.*?)</p>',res.text,re.S)
# print(content)