

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

smtp = smtplib.SMTP_SSL('smtp.163.com', 465)

msg = MIMEMultipart('alternative')  # 实例化email对象

msg.attach(MIMEText('Hello World!', 'html'))

with smtplib.SMTP_SSL('smtp.163.com', 465) as smtp:
    smtp.ehlo()  # 用户认证
    smtp.login('xiaofeilife', 'QJLSKQWYKXYIOFOA')  # 括号中对应的是发件人邮箱账号、邮箱密码
    smtp.sendmail('xiaofeilife@163.com', 'xiaofeilife@163.com', str(msg))  # 收件人邮箱账号、发送邮件