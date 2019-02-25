#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.error import URLError, HTTPError
import urllib.request
import re
import time
import pymysql

class GetAndStore:
    def __init__(self):
        pass

    #function
    def printHotNews(self,url):
        content = urllib.request.urlopen(url).read().decode('utf-8')
        pattern = re.compile('<li class="hd.*?<strong>.*?<a.*?>(.*?)</a>.*?strong>', re.S)
        hotNews = re.findall(pattern, content)
        for i in hotNews:
            print(i)
        return hotNews

    #function can be reused
    def storeDB(self,table,news):
        #use dict store news
        news_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        news_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #test insert only 1 record
        text = "'" + news[0] + "'"  #Chinese character and symbol
        time_now = "'" + news_time + "'"
        date = "'" + news_date + "'"

        #connect mysqlDB
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='mydb',
            charset='utf8')

        try:
            with conn.cursor() as cursor:
                #create a table
                sql = """CREATE TABLE IF NOT EXISTS %s (
                            text  VARCHAR(200),
                            time  VARCHAR(200),
                            date VARCHAR(200))""" % (table,)
                cursor.execute(sql)
                # Create a new record
                sql = "INSERT INTO %s (%s,%s,%s) VALUES (%s,%s,%s)" % (table, 'text', 'date', 'time', text, date, time_now)
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()

            with conn.cursor() as cursor:
                # Read all records
                sql = "SELECT * FROM (%s) " %(table,)
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                cursor.close()
        finally:
            conn.close()


if __name__ == "__main__":
    #variable
    url = 'http://news.baidu.com/'
    instance1 = GetAndStore()  #create an instance

    try:
        response = urllib.request.urlopen(url)
    except HTTPError as e:
        # http error
        print('Error code: ', e.code)
    except URLError as e:
        # url error
        print('Reason: ', e.reason)
    else:
        # excute function
        instance1.printHotNews(url)
        instance1.storeDB("table1", instance1.printHotNews(url))