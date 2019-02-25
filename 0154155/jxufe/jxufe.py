import requests
from bs4 import BeautifulSoup
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url = 'http://www.jxufe.edu.cn/'
res = requests.get(url,headers = headers)
soup = BeautifulSoup(res.content,'lxml')
print(soup)