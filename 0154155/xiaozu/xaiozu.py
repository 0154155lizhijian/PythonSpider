from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

def judgment_sex(class_name):
    if class_name == ['member_ico1']:
        return '女'
    else:
        return '男'

'''def get_links(url):
    wb_data = requests.get(url,headers=headers)
    print('1')
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list>ul>li>a')
    for link in links:
        href = link.get("href")
        get_info(href)
        print('2')'''
def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    tittles = soup.select('div.pho_info>h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart>div.day_1>span')
    imgs = soup.select('#floatRightBox>div.js_box.clearfix>div.member_pic>a>img')
    name = soup.select('#floatRightBox>div_js_box.clearfix>div.w_240>h6>a')
    sex = soup.select('#floatRightBox>div.js_box.clearfix>div.member_pic>div')
    print('3')
    for tittles,addresses,prices,imgs,name,sex in zip(tittles,addresses,prices,imgs,name,sex):
        data = {
            'tittles':tittles.get_text().strip(),
            'addresses':addresses.get_text().strip(),
            'prices':prices.get_text,
            'imgs':imgs.get("src"),
            'name':name.get_text(),
            'sex':judgment_sex(sex.get("class"))
        }
        print(data)
        print('4')

if  __name__ == '__main__':
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,14)]
    for url in urls:
        get_info(url)
        time.sleep(2)