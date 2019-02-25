import requests
from lxml import etree
import pymysql
from multiprocessing import Pool
import time

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mydb', port=3306, charset='utf8')
cursor = conn.cursor()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

def get_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@id="list-container"]/li')
    for info in infos:
        try:
            author = info.xpath('div/div[1]/div/a/text()')[0]
            publish_time = info.xpath('div/div[1]/div/span/text()')[0]
            title = info.xpath('div/a/text()')[0]
            content = info.xpath('/div/p/text()')[0].strip()
            view = info.xpath('div/div[2]/a[1]/text()')[0].strip()
            comment = info.xpath('div/div[2]/a[2]/text()')[0].strip()
            like = info.xpath('div/div[2]/span/text()')[0].strip()
            rewards = info.xpath('/div/div[2]/span[2]/text()')
            if len(rewards) == 0:
                rewards = 'null'
            else:
                rewards = rewards[0].strip()
            cursor.execute("insert into jianshuone (author,publish_time,title,content,view,comment,like,rewards) values (%s,%s,%s,%s,%s,%s,%s,%s) ",(str(author), str(publish_time), str(title), str(content), str(view), str(comment), str(like), str(rewards)))
        except IndexError:
            pass
        print('2')
        print('3')

if __name__ == '__main__':
    urls=['https://www.jianshu.com/c/bDHhpK?order_by=added_at&page={}'.format(str(i)) for i in range(1,100)]
    pool = Pool(processes=4)
    pool.map(get_info, urls)
    print('a')
    print('1')
    conn.commit()