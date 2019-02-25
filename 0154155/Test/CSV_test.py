import csv
fp = open('C:\\Users\\李智坚\\Desktop\\py.file\\test.csv','w+')
writer = csv.writer(fp)
writer.writerow(('id', 'name'))
writer.writerow(('1', 'z'))

