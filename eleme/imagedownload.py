import os
import urllib.request
import requests
import json
import time
from bs4 import BeautifulSoup

import urllib.error
import urllib3
import pymysql
id_list = []#店铺的id列表
name_list = []#店铺的名称列表
address_list = []#店铺的地址列表
info_list = []
image_path_list=[]
typename_list = []
goodsname_list = []
price_list = []
month_sales = []
goods_description =[]
goods_image_path = []

# shopid_list = []
# for a in range(0,48):
#     a=a+1
#     shopid_list.append(a)
# print(shopid_list)


x=0


def auto_down(url, filename):
    import socket
    import urllib.request
    # 设置超时时间为30s
    socket.setdefaulttimeout(30)
    # 解决下载不完全问题且避免陷入死循环
    try:
        urllib.request.urlretrieve(url, filename)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(url, filename)
                break
            except socket.timeout:
                err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                print(err_info)
                count += 1
        if count > 5:
            print("downloading picture fialed!")
# conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='eleme', port=3306, charset='utf8')
# print('已连接')
# cursor = conn.cursor()
def get_all_id():
    for offset in range(0,24,24):
        url='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wx4g06hu38n&latitude=24.609607&limit=24&longitude=118.042858&offset={}&terminal=web'.format(offset)
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
            restaurant_description = item.get('description')
            info_list.append(restaurant_description)
            restaurant_image_path = item.get('image_path')
            image_path_list.append(restaurant_image_path)
            # try:
            #     image_path = image_path_list[x-1]
            #     image_type = image_path[32:]
            #     image_url = "http://fuss10.elemecdn.com/" + image_path + "." + image_type
            #     urllib.request.urlretrieve(image_url, 'D:/img/' + image_path + '.jpg')
            #     time.sleep(1)
            #     print(1)
            # except:
            #     print('错误')
            #     pass

    return id_list,image_path_list
get_all_id()
m=0#用来计数，第几个店铺
n=0#用来记录数据，第几条数据
i=0
k=0
for id in id_list:
    m=m+1
    restaurant_url = 'https://mainsite-restapi.ele.me/shopping/v2/menu?restaurant_id='+str(id)
    print('*************************这里是店铺分界线******第{}个店铺*********************************************'.format(m))

    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    web_data = requests.get(restaurant_url,headers=headers)
    time.sleep(1)
    content = web_data.text
    json_obj = json.loads(content)

    for item in json_obj:
        for food in item.get('foods'):
            restaurant_goods_image_path = food.get('image_path')
            goods_image_path.append(restaurant_goods_image_path)

            g_image_path = goods_image_path[i - 1]
            print(g_image_path)
            try:
                g_image_type = g_image_path[32:]
                print(g_image_type)
                g_image_url = "http://fuss10.elemecdn.com/" + g_image_path + "." + g_image_type
                auto_down(g_image_url,'D:/img/' + g_image_path + '.jpg')
                # urllib.request.urlretrieve(image_url, 'D:/img/' + g_image_path + '.jpg')
                print('成功')
            except:
                pass


print('ok')
#


#


