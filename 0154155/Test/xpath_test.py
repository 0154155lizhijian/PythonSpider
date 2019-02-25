import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

url = 'https://www.qiushibaike.com/text'
res = requests.get(url,headers=headers)
selector = etree.HTML(res.text)
infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
'''for info in infos:
    for i in range(0,10):
        name = info.xpath('//div[1]/a[2]/h2/text()')
        name[i] = info.xpath('//div[1]/a[2]/h2/text()')[i]
        print(name[i])'''
for info in infos:
    names = info.xpath('//div[1]/a[2]/h2/text()')
for name in names:
    print(name)



