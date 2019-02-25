import requests
from lxml import etree
import time
import xlwt


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

all_info_list = []
def get_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for info in infos:
            bookname = info.xpath('div[2]/h4/a/text()')[0]
            author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
            type_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
            type_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
            booktype = type_1 + '|' + type_2
            bookstate = info.xpath('div[2]/p[1]/span/text()')
            content = info.xpath('div[2]/p[2]/text()')[0].strip()
            number = info.xpath('div[2]/p[3]/span/span/text()')[0]
            info_list = [bookname, author, booktype, bookstate, content, number]
            all_info_list.append(info_list)


if __name__ == '__main__':
    urls =['https://www.qidian.com/all/?page={}'.format(str(i)) for i in range(1,100)]
    for url in urls:
        get_info(url)
    header = ['bookname', 'author', 'booktype', 'bookstate', 'content', 'number']
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    i = 1
    for list in all_info_list:
        j=0
        for data in list:
            sheet.write(i, j, data)
            j += 1
        i += 1
book.save('xiaoshuo.xls')

