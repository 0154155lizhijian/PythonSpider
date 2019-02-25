
#commentsUrl用于获取新闻评论数等json信息
import datetime
import json
import re

import requests
from bs4 import BeautifulSoup

commentsUrl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1487565938347_44362583'

#获取评论数量的函数
def getCommentsCount(newsUrl):
    before = re.escape('doc-i')
    after = re.escape('.shtml')
    m = re.search(before + '(.+)' + after, newsUrl)
    newsId = m.group(1)
    comments = requests.get(commentsUrl.format(newsId))
    jd = json.loads(comments.text.strip('var loader_1487565938347_44362583='))
    commentCount = jd['result']['count']['total']
    return commentCount

#获取新闻具体内容的函数
def getNewsDetail(newsUrl):
    result = {}
    res = requests.get(newsUrl)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newsSource'] = source = soup.select('#navtimeSource span a')[0].text
    timesource = soup.select('#navtimeSource')[0].contents[0].strip()
    result['newsTime'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article'] = '\n'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
    result['commentsCount'] = getCommentsCount(newsUrl)
    return result

#测试
result = getNewsDetail('http://news.sina.com.cn/c/nd/2017-02-20/doc-ifyarrcf4846170.shtml')
print(result)