#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from readConfig import *

'''发送邮件'''


c=ReadConfig('../fileConfig/config.ini')
sender=c.get_email('sender')
pwd=c.get_email('pwd')
receivers=c.get_email('receivers')
mail_host=c.get_email('mail_host')
mail_port=c.get_email('mail_port')
filePath=c.get_email('filePath')
subject=c.get_email('subject')
print(filePath)
class SendMail:

    def send(self):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("测试结果", 'utf-8')
        message['To'] = Header("测试", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是测试结果……', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 testapi.txt 文件
        att1 = MIMEApplication(open(r'D:\pyworkspace\testapi\report\allurehtml\index.html', 'rb').read(), 'base64')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="index.html"'
        message.attach(att1)

        # 构造附件2，传送当前目录下的 runoob.txt 文件
        att2 = MIMEApplication(open('../fileConfig/qq.png', 'rb').read(), 'base64')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="qq.png"'
        message.attach(att2)

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host,mail_port)
            smtpObj.login(sender,pwd)
            smtpObj.sendmail(sender,receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

if __name__=='__main__':
    c=SendMail()
    c.send()


