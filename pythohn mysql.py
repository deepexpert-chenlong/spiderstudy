#__author__ = 'lenove'
#coding:utf-8
import urllib
import urllib2
import requests
import re
import MySQLdb
def all():
    a = []
    for n1 in range(97,123):
        for n2 in range(97,123):
            for n3 in range(97,123):
                for n4 in range(97,123):
                    for n5 in range(97,123):
                        a.append(chr(n1)+chr(n2)+chr(n3)+chr(n4)+chr(n5))
    return a

def getvalue(html):
    req = '<tr height=.*?value=\'(.*?)\' />'
    list = re.compile(req).findall(html)
    for value in list:
        return value

connect = MySQLdb.connect(host='localhost', user='root', passwd='wszgr728', db='test')
cur=connect.cursor()
cur.execute('CREATE TABLE results(site VARCHAR(8),suffix VARCHAR(8))')
a = all()
for x in a:
    suffix = '.com'
    data = {'d_name':x+suffix,'dtype':'common'}
    html = requests.post('http://www.zgsj.com/domain_reg/domaintrans.asp',data)
    value = getvalue(html.content)
    if(value == 'no'):
        values = [x,suffix]
        cur.execute("INSERT INTO results VALUES(%s, %s)" ,values)
        connect.commit()
        print '可用域名:'+x+'.com'
connect.close()

