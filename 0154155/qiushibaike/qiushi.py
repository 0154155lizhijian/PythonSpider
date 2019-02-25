
import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
info_lists = []
def judgement_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'



def get_info(url):
    respond = requests.get(url,headers=headers)
    names = re.findall('div class="article block untagged mb15 .*?>.*?<h2>\n(.*?)\n</h2>.*?</div>',respond.text,re.S)
    ages = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',respond.text,re.S)
    sexs  =re.findall('<div class="articleGender (.*?)">',respond.text,re.S)
    contents = re.findall('<div class="content">.*?<span>\n\n\n(.*?)</span>.*?</div>',respond.text.encode('GBK','ignore').decode('GBk'),re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',respond.text,re.S)
    comments =re.findall('<i class="number">(\d+)</i> 评论',respond.text ,re.S)

    for age, name, sex, content, laugh, comment in zip(ages, names, sexs, contents, laughs, comments):
        info = {
            'name': name,
            'age': age,
            'sex': judgement_sex(sex),
            'content': content,
            'laugh': laugh,
            'comment': comment
        }
        info_lists.append(info)


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 2)]
    for url in urls:
        get_info(url)
    for info_list in info_lists:
        try:
            f = open('C:\\Users\\李智坚\\Desktop\\py.file\\qiushi.txt','a+')
            f.write(info_list['name']+'\n')
            f.write(info_list['age'] + '\n')
            f.write(info_list['sex'] )
            f.write(info_list['content'] + '\n')
            f.write(info_list['laugh'] + '\n')
            f.write(info_list['comment'] + '\n\n')
            f.close()
        except UnicodeEncodeError:
            pass
