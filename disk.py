#!/usr/bin/env pytho# -*- coding: utf-8 -*- 

from __future__ import division
import smtplib
from email.mime.text import MIMEText
import os

class Disk_Model:

    def __init__(self):
        self.mail_host = "smtp.163.com"
        self.mail_user = "邮箱@之前"
        self.mail_pass = "邮箱密码"
        self.postfix = "163.com"

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

    def disk_mnt(self):
        disk = os.statvfs('/usr/local')
        percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks - disk.f_bfree + disk.f_bavail)
        return percent

mailto_list=["+++++@qq.com", "++++++++++++@163.com"]

disc = Disk_Model()
if disc.disk_mnt() > 95:
    if disc.send_mail(mailto_list, '报警邮件系统磁盘/usr/local', "/usr/local 使用率已经超过95%,请及时清理"):
        print "报警邮件发送成功"
    else:
        print "报警邮件发送失败"
else:
    perc = round(disc.disk_mnt())
    print '当前磁盘使用 %s%%'%perc
    per = '/usr/local 使用率没有超过95%不发送报警邮件'
    print per
