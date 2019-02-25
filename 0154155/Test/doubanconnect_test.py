import requests
from bs4 import BeautifulSoup
import time

headers = {
   'User - Agent' : 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87Safari / 537.36'
}

url = 'https://www.qidian.com/rank'
res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text,'lxml')
print(html)