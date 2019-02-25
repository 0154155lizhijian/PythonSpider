import json
import os
from urllib.parse import urlencode
import pymysql
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, RequestException
import re
from multiprocessing import Pool
from hashlib import md5
from json.decoder import JSONDecodeError


# conn = pymysql.connect(host='localhost',user = 'root',passwd='123456',db='mydb',port = 3306,charset='utf8')
# cursor = conn.cursor()

def get_page_index(offset, keyword):
    data = {
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3,
        'format': 'json',
        'keyword': keyword,
        'offset': offset,
    }
    params = urlencode(data)
    base = 'http://www.toutiao.com/search_content/'
    url = base + '?' + params
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None


# def download_image(url):
#     print('Downloading', url)
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             save_image(response.content)
#         return None
#     except ConnectionError:
#         return None
#
#
# def save_image(content):
#     file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
#     print(file_path)
#     if not os.path.exists(file_path):
#         with open(file_path, 'wb') as f:
#             f.write(content)
#             f.close()
#
#
def parse_page_index(html):
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('Error occurred',url)
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('var gallery = (.*?);', re.S)
    result = re.search(images_pattern, html)
    if result:
        print(result.group(1))
        # data = json.loads(result.group(1))#.replace('\\', ''))
        # if data and 'sub_images' in data.keys():
        #     sub_images = data.get('sub_images')
        #     images = [item.get('url') for item in sub_images]
        #     # for image in images: download_image(image)
        #     return {
        #         'title': title,
        #         'url': url,
        #         'images': images
        #     }





def main():
    html = get_page_index(0, '街拍')
    urls = parse_page_index(html)
    for url in urls:
        html = get_page_detail(url)
        if html:
            parse_page_detail(html, url)
            print('1')
            print('1')



if __name__ == '__main__':
    main()
    # pool = Pool()
    # groups = ([x * 20 for x in range(1, 20)])
    # pool.map(main, groups)
    # pool.close()
    # pool.join()
