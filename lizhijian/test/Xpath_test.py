import requests
from lxml import html

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

url = 'https://www.qiushibaike.com/text/'
res = requests.get(url,headers=headers)
selector = html.etree.HTML(res.text)
url_info = selector.xpath('//*[@id="qiushi_tag_120253021"]/div[2]/span[1]/i/text()')
print(url_info)
