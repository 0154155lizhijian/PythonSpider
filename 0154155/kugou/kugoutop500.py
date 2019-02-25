import requests
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    name = soup.select('div.pc_temp_songlist > ul > li > a')
    # -*- coding:utf-8 -*-

    '''zzr = soup.find_all('ul', class_=" ")
    for item in zzr:
        list_tmp = item.find_all('a')
        for a in list_tmp:
            print(a.get('href') )'''
    for ranks, name in zip(ranks, name):
        data = {
            'rank': ranks.get_text().strip(),
            'singer': name.get_text().split('-')[0],
            'song': name.get_text().split('-')[1]
            # 'link':zzr.get_text().strip()
        }
        print(data)


if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(number) for number in range(1, 24)]
    pool = Pool(processes=2)
    pool.map(get_info,urls)
    # for url in urls:
    #     get_info(url)
    time.sleep(1)
