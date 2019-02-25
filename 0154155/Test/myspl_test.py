import pymysql

conn = pymysql.connect(host='localhost',user = 'root',passwd='123456',db='mydb',port = 3306,charset='utf8')
cursor = conn.cursor()
cursor.execute("insert into student (name,sex,grade) values(%s,%s,%s)",('李大 ','女',87))
conn.commit()
