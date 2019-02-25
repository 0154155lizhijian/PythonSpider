import requests
from urllib.parse import urlencode
from multiprocessing.pool import Pool
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)"
                  "AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
}


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '科技',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url, headers)
        # print(response.status_code)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None




def get_news(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('open_url') is None:
                continue
            images = []
            for image in item.get("image_list"):
                image['url'] = 'http:' + image['url']
                images.append(image['url'])
            author = item.get('media_name')
            author_id = item.get('id')
            comments = item.get('comments_count')
            contents = item.get('article_url')
            date = item.get('datetime')
            images = images
            title = item.get('title')
            new_id = item.get('item_id')
            yield {
                'author': author,
                'author_id': author_id,
                'comments': comments,
                'contents': contents,
                'date': date,
                'images': images,
                'title': title,
                'new_id': new_id
            }


def save_news(item, offset):
    with open('data.json', 'a') as f:
        data = json.dumps(item)
        f.write(data + '\n')
    print(data)


def main(offset):
    json = get_page(offset)
    # print(get_news(json))
    for item in get_news(json):
        # print(item)
        save_news(item, offset)


GROUP_START = 0
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    # print(groups)
    pool.map(main, groups)
    print('保存完成！')
    pool.close()
    pool.join()
