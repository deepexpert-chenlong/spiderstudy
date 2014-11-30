__author__ = 'Lenovo'
#coding:utf-8
import time
import requests
import re
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendmail(to_list,sub,con):
  """发送邮件
  """
# 设置服务器名称、用户名、密码以及邮件后缀s
  mail_host="smtp.163.com"
  mail_user="*****@163.com"
  mail_pass="*****"
  mail_postfix="mail.163.com"

  me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
  msg = MIMEMultipart('related')
  msg['Subject'] = email.Header.Header(sub,'utf-8')
  msg['From'] = me
  msg['To'] = ";".join(to_list)
  msg.preamble = 'This is a multi-part message in MIME format.'

  msgAlternative = MIMEMultipart('alternative')
  msgText = MIMEText(con, 'plain', 'utf-8')
  msgAlternative.attach(msgText)
  msg.attach(msgAlternative)

  try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user,mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()

  except Exception,e:
    return False
  return True
url = 'http://store.apple.com/hk-zh/buy-iphone/iphone5s'
while 1:
    html = requests.get(url)
    reg = '{"dimensionColor":"(.*?)","dimensionCapacity":"(.*?)","partNumber":".*?","price":"(.*?)","displayShippingQuote":"(.*?)".*?}'
    r=re.compile(reg)
    mes = r.findall(html.text)
    for i in mes:
        print i[0]+'   ',i[1]+'   ','HK$'+i[2]+'   '+i[3]
        if i[3].encode('utf-8') == '有現貨':
            text = 'iphone5s有现货:'+'  颜色：'+i[0].encode('utf-8')+'  内存空间：'+i[1].encode('utf-8')+'  价格：HK$'+i[2].encode('utf-8')
            if sendmail(['*****@139.com'],"订购iphone",text):
                print "信息已经成功发送到xxx@139.com"
            else:
                print "邮件发送失败!"
    print "10秒刷新一次"
    time.sleep(10)
