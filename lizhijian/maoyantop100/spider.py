import requests
import re
from bs4 import BeautifulSoup


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
def get_one_page(url):
        response = requests.get(url,headers=headers)
        html = BeautifulSoup(response.text,'lxml')
        pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name"><a'
                        +'.*?>（.*?）</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
        items = re.findall(pattern,html)
        print(items)
if __name__ == '__main__':
    url = 'http://maoyan.com/board/4?'
    get_one_page(url)