# 引入相关模块
import requests
from bs4 import BeautifulSoup
import re

url = "http://news.qq.com/"
# 请求腾讯新闻的URL，获取其text文本
wbdata = requests.get(url).text
# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata,'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.text > em.f14 > a.linkto")

# 对返回的列表进行遍历
# def get_content(link_url):
#     res = requests.get(link_url).text
#     # 对获取到的文本进行解析
#     selector = BeautifulSoup(res, 'lxml')
#     content = selector.select("div.content-article>p.one-p")
#     x = content.get_text(content)
#     print(content)


for n in news_titles:
    # 提取出标题和链接信息
    title = n.get_text()
    link_url = n.get("href")
    res = requests.get(link_url)
    # 对获取到的文本进行解析
    content = re.findall('<p class="one-p">.*?(.*?)</p>',res.text,re.S)


    # print(content)


    # for link in links:


    data = {
        '标题':title,
        '链接':link_url,
        '时间':time,
        '内容':content
    }
    print(data)

