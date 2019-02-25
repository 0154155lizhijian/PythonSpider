import requests
import re
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

f = open('C:\\Users\李智坚\\Desktop\\doupo.txt','a+')

def get_info(url):
    respond = requests.get(url,headers=headers)
    if respond.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',respond.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')
    else:
        pass

if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(number) for number in range(2,1665)]
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()

