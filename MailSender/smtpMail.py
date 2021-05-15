# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/2/18 11:51
# author:Sabo
import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = 'senderQQNumber@qq.com'

receiver = 'receiverQQNumber@qq.com'

subject = 'python main test'

smtpserver = 'smtp.qq.com'
username = sender
password = 'Your QQ password'

msg = MIMEText('你好，这是python自动邮件测试','text','utf-8')
msg['Subjectr'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')

smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
