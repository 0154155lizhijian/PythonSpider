# coding: utf-8

import codecs
from urllib import request, parse
from bs4 import BeautifulSoup
import re
import time
from urllib.error import HTTPError, URLError
import sys


###新闻类定义
class News(object):
    def __init__(self):
        self.url = None  # 该新闻对应的url
        self.topic = None  # 新闻标题
        self.date = None  # 新闻发布日期
        self.content = None  # 新闻的正文内容
        self.author = None  # 新闻作者



def getNews(url):
    # 获取页面所有元素
    html = request.urlopen(url).read().decode('utf-8', 'ignore')
    # 解析
    soup = BeautifulSoup(html, 'html.parser')

    # 获取信息
    if not (soup.find('div', {'id': 'artical'})): return

    news = News()  # 建立新闻对象

    page = soup.find('div', {'id': 'artical'})

    if not (page.find('h1', {'id': 'artical_topic'})): return
    topic = page.find('h1', {'id': 'artical_topic'}).get_text()
    news.topic = topic

    if not (page.find('div', {'id': 'main_content'})): return
    main_content = page.find('div', {'id': 'main_content'})

    content = ''

    for p in main_content.select('p'):
        content = content + p.get_text()

    news.content = content

    news.url = url  # 新闻页面对应的url
    f.write(news.topic + '\t' + news.content + '\n')


##dfs算法遍历全站###
def dfs(url):
    global count
    print(url)

    pattern1 = 'http://news\.ifeng\.com\/[a-z0-9_\/\.]*$'  # 可以继续访问的url规则
    pattern2 = 'http://news\.ifeng\.com\/a\/[0-9]{8}\/[0-9]{8}\_0\.shtml$'  # 解析新闻信息的url规则


    if url in visited:  return
    print(url)


    visited.add(url)
    # print(visited)

    try:

        html = request.urlopen(url).read().decode('utf-8', 'ignore')
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')

        if re.match(pattern2, url):
            getNews(url)
            # count += 1

        ####提取该页面其中所有的url####
        links = soup.findAll('a', href=re.compile(pattern1))
        for link in links:
            print(link['href'])
            if link['href'] not in visited:
                dfs(link['href'])
                # count += 1
    except HTTPError as e:
        print(e)
        return
        # print(count)
    except URLError as e:
        print(e)
        return
    # if count > 3: return


visited = set()

f = open('C:\\Users\\李智坚\\.txt', 'a+', encoding='utf-8')

dfs('http://news.ifeng.com/')