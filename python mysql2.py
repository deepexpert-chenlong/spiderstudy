#__author__ = 'lenove'
#coding:utf-8
import urllib
import urllib2
import requests
import re
import MySQLdb
import time
url1 = 'http://hq.sinajs.cn/?rn=1417610216083&list=USDCNY'
url2 = 'http://hq.sinajs.cn/?rn=1417610565584&list=DINIW'

html1 = requests.get(url1)
html2 = requests.get(url2)

rate = re.compile('var hq_str_USDCNY=".*?,(.*?),.*?";').findall(html1.text)
dollar = re.compile('".*?,(.*?),.*?";').findall(html2.text)

value = []
value.append(rate[0].encode('utf-8'))
value.append(dollar[0].encode('utf-8'))

try:
    cxn = MySQLdb.connect(host='localhost', user='root', passwd='wszgr728',db='test')
except:
    print "Could not connect to MySQL server."
    exit(0)

cur = cxn.cursor()
cur.execute("CREATE TABLE RESULT(rate VARCHAR(8),dollar VARCHAR(8))")

while 1:
    cur = cxn.cursor()
    cur.execute("INSERT INTO result values(%s,%s)",value)
    cxn.commit()
    print 'writing...'
    time.sleep(3600)

cxn.close()

