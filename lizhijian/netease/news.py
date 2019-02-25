import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'http://news.163.com/world/'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
res = requests.get(url,headers = headers)
# selector = etree.HTML(res.text)
#
# title = selector.xpath('//*[@class="news_title"]/h3/text()')
# #('//html/body/div[1]/div[3]/div[4]/div[1]/div/div/ul/li/div/div[2]/div/div[1]/h3/a/text()')
# print(title)
soup = BeautifulSoup(res.text,'lxml')
# print(soup)
# for news in soup.select('div.news_title'):
#     # h3 = news.select('h3>a')
#     #
#     # if len(h3) > 0:
#     title = news.select('h3>a')
#     # href = h2[0].select('a')[0]['href']
#     print(title)


selector = soup.find_all('ul',"idx_cm_list idx_cm_list_h")
# title = soup.select('body > div.second2016_wrap.guoji_second_wrap > div.second2016_content > div.ns_area.second2016_main.clearfix > div.second_left > div > div > ul > li > div > div:nth-of-type(5) > div > div.news_title > h3 > a')
for news in selector:
    title = news.select( '#li> a')
    print(title)


