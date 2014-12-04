#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import smtplib
from email.mime.text import MIMEText

class Mail_Model:

    def __init__(self):
        self.mail_host = "smtp.163.com"
        self.mail_user = "发件邮箱名称"
        self.mail_pass = "发件邮箱密码"
        self.postfix = "发件邮箱后缀@XXXX.com"

    def send_mail(self, to_list, sub, content):
        me = "hello"+"<"+self.mail_user+"@"+self.postfix+">"
        msg = MIMEText(content, _subtype = 'html', _charset = 'utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ';'.join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False

    def start(self):
        print 'hello world'

mailto_list=["XXXXXXXXX@qq.com", "XXXXXXXXXXX@163.com"]

mail = Mail_Model()
if mail.send_mail(mailto_list, 'testing', "<a href='http://www.baidu.com'>百度</a>"):
    print "发送成功"
else:
    print "发送失败"
