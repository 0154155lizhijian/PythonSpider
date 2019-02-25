import os
import urllib.request
import requests
import json
import time
from bs4 import BeautifulSoup
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

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='eleme', port=3306, charset='utf8')
print('已连接')
cursor = conn.cursor()
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
def get_all_id():
    for offset in range(0,48,24):
        url='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wx4g06hu38n&latitude=28.717397&limit=24&longitude=115.829852&offset={}&terminal=web'.format(offset)
        web_data = requests.get(url)
        soup=BeautifulSoup(web_data.text,'lxml')
        content = soup.text
        print(content)
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
            try:
                image_path = image_path_list[x-1]
                image_type = image_path[32:]
                image_url = "http://fuss10.elemecdn.com/" + image_path + "." + image_type
                auto_down(image_url, 'D:/img/' + image_path + '.jpg')
            except:
                pass
    return name_list,address_list,id_list,info_list,image_path_list
get_all_id()
m=0#用来计数，第几个店铺
n=0#用来记录数据，第几条数据
i=0
k=0
for id in id_list:
    m=m+1
    restaurant_url = 'https://mainsite-restapi.ele.me/shopping/v2/menu?restaurant_id='+str(id)
    print('*************************这里是店铺分界线******第{}个店铺*********************************************'.format(m))

    cursor.execute("INSERT into shop VALUES(null,'" + name_list[m - 1] + "','" + info_list[m - 1] + "',1,'" + address_list[m - 1] + "',1,'" + image_path_list[m - 1] + "','营业中')")
    cursor.execute("select sid from shop where sname='" + name_list[m - 1] + "' and saddress = '" + address_list[m - 1] + "'")
    sid = cursor.fetchall()
    getsid = str(sid[0][0])
    print(getsid)
    conn.commit()

    # print(name_list[m])
    # print(address_list[m])
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    web_data = requests.get(restaurant_url,headers=headers)
    #time.sleep(3)
    content = web_data.text
    json_obj = json.loads(content)

    for item in json_obj:
        n +=1
        restaurant_typename = item.get('name')
        typename_list.append(restaurant_typename)
        print(typename_list[n-1])

        try:
            cursor.execute("INSERT into goodstype VALUES(null,'" + typename_list[n-1]+ "','" + getsid+ "')")
            cursor.execute("select gtid from goodstype where gtname='" + typename_list[n-1] + "' ")
            print(2)
            gtid = cursor.fetchall()
            getgtid = str(gtid[0][0])
            print(getgtid)
        except:
            pass
        conn.commit()


        for food in item.get('foods'):
            i +=1
            restaurant_goodsname = food.get('name')
            goodsname_list.append(restaurant_goodsname)
            print(goodsname_list[i-1])

            restaurant_month_sales = food.get('month_sales')
            month_sales.append(restaurant_month_sales)
            print(month_sales[i - 1])

            restaurant_goods_description = food.get('description')
            goods_description.append(restaurant_goods_description)
            print(goods_description[i - 1])

            restaurant_goods_image_path = food.get('image_path')
            goods_image_path.append(restaurant_goods_image_path)
            # print(goods_image_path[i - 1])
            g_image_path = goods_image_path[i - 1]
            print(g_image_path)
            try:
                g_image_type = g_image_path[32:]
                print(g_image_type)
                g_image_url = "http://fuss10.elemecdn.com/" + g_image_path + "." + g_image_type
                auto_down(g_image_url, 'D:/img/' + g_image_path + '.jpg')
                # urllib.request.urlretrieve(image_url, 'D:/img/' + g_image_path + '.jpg')
                print('成功')
            except:
                pass

            for specfood in food.get('specfoods'):
                k +=1
                restaurant_price = specfood.get('price')
                price_list.append(restaurant_price)
                print('价格：'+str(price_list[k-1]))
            try:
                cursor.execute("INSERT into goods VALUES(null,'" + goodsname_list[i - 1] + "','" + str(price_list[k-1]) + "','" + str(month_sales[i-1]) + "','" + goods_description[i-1] + "','//fuss10.elemecdn.com/"+goods_image_path[i-1]+".jpeg?imageMogr2/thumbnail/100x100/format/webp/quality/85',1,'" + getgtid+ "')")
                print(3)
            except:
                pass
            conn.commit()
            try:
                cursor.execute("INSERT into shopuser VALUES(null,'"+str(getsid)+"',FLOOR((RAND()*100)*10+1),FLOOR((RAND()*100)*10+1))")
            except:
                pass
conn.close()