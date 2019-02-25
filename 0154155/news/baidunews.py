import requests
from lxml import etree
from bs4 import BeautifulSoup


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
# all_info_list = []
def get_news_url(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    news_herfs = selector.xpath('//div/div/ul/li/strong/a/@href')
    # titles = selector.xpath('//div/div/ul/li/strong/a/text()')

    for news_herf in news_herfs:
        get_news_info(news_herf)
        print(news_herf)

def get_news_info(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.content)
    try:
        # title = selector.xpath('/html/body/div/div/div//h1/text() ')[0]
        # title1 = selector.xpath('/html/body/div/div/div/div/div/div/span/text()')[0]
        news_time = selector.xpath('/html/body/div[7]/div[3]/div[1]/div/span[1]/i/text()')[0]
        # content = selector.xpath('div[@class="col_w660"]/p/text()')
        # info_list=[title, news_time]
        # all_info_list.append(info_list)
        print(news_time)

        # cursor.execute("insert into doubanmovie (name,director,actor,style,country,release_time,time,score) values (%s,%s,%s,%s,%s,%s,%s,%s) ",(str(name), str(director), str(actor), str(style), str(country), str(release_time), str(time), str(score)))
    except IndexError:
        pass


if __name__ == '__main__':
    url = 'https://news.baidu.com/'
    get_news_url(url)