import requests
from bs4 import BeautifulSoup
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url = 'https://www.77kp.com/'
res = requests.get(url,headers = headers)
res.encoding = 'utf-8'
selector = etree.HTML(res.text)
# soup = BeautifulSoup(res.text,'lxml')
names = selector.xpath('//ul/li/a/text()')
get_urls = names.xpath('/@href')
# for get_url in get_urls :
#     try:
#         get_url = get_url.strip('/')
#         respond = requests.get('https://www.77kp.com/get_url')
#         # res.encoding = 'utf-8'
#         soup = BeautifulSoup(respond.content,'lxml')
#         print(soup)
#     except:
#         pass
    # selector1 = etree.HTML(respond.text)
    # picture = selector1.xpath('//table/tbody/tr/td/div/h2/text()')
    # print(picture)
#
for name ,get_url in zip (names ,get_urls):
    data = {
        '剧名': name,
        '链接':get_url.strip('/')
    }
    print(data)
