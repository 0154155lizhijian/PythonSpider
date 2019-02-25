#-*-coding:utf8-*-
import sys
from imp import reload

import requests
from bs4 import BeautifulSoup
import json
from lxml import etree
# reload(sys)
# sys.setdefaultencoding('gbk')
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
info_lists = []
lists=['a','b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z']
for i in lists:
 urls = ['http://product.auto.163.com/brand/{}/'.format(i) ]

 for url in urls:
  # print(url)
  res = requests.get(url,headers=headers)
  car = res.content
  selector = etree.HTML(car)
  imgs = selector.xpath('//*[@id="qcdq_brand2"]/div[1]/div[2]/div[2]/ul/li/a/img/@src')
  names = selector.xpath('//*[@id="qcdq_brand2"]/div[1]/div[2]/div[2]/ul/li/a/img/@alt')
  for img,name,car_type in zip(imgs,names,lists):
   info={
    'img':img,
    'name':name,
    'car_type':i,
    'ishot': bool(0)
   }
   # print(info)
   with open('info.json', 'a',encoding='utf-8') as f:
    info = json.dumps(info,ensure_ascii=False)
    print(info)
    f.write(info + '\n')



