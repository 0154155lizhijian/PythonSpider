# -*- coding: utf-8 -*-
# @Time    : 2017/12/10 15:35
# @Author  : Ricky
# @FileName: final_version.py
# @Software: New_start
# @Blog    ：http://www.cnblogs.com/Beyond-Ricky/

import requests
import json
import time
from bs4 import BeautifulSoup
import lxml
id_list = []#店铺的id列表
name_list = []#店铺的名称列表
address_list = []#店铺的地址列表

def get_all_id():
    for offset in range(0,985,24):
        url='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wx4g06hu38n&latitude=39.91406&limit=24&longitude=116.38477&offset={}&terminal=web'.format(offset)
        web_data = requests.get(url)
        soup=BeautifulSoup(web_data.text,'lxml')
        content = soup.text
        json_obj = json.loads(content)
        for item in json_obj:
            restaurant_address = item.get('address')
            address_list.append(restaurant_address)
            restaurant_name = item.get('name')
            name_list.append(restaurant_name)
            restaurant_id = item.get('id')
            id_list.append(restaurant_id)
    return name_list,address_list,id_list
get_all_id()
m=0#用来计数，第几个店铺
n=0#用来记录数据，第几条数据
for id in id_list:
    m=m+1
    restaurant_url = 'https://mainsite-restapi.ele.me/shopping/v2/menu?restaurant_id='+str(id)
    print('*************************这里是店铺分界线******第{}个店铺*********************************************'.format(m))

    print(name_list[m])
    print(address_list[m])
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    web_data = requests.get(restaurant_url,headers=headers)
    #time.sleep(3)
    content = web_data.text
    json_obj = json.loads(content)
    try:
        for item in json_obj:
            for food in item.get('foods'):

                n +=1
                print('第%d条数据:' % n)
                print(food.get('name'),food.get('tips'),'评分',food.get('rating'))
    except AttributeError as e :
        pass
    except IndexError as e1:
        pass