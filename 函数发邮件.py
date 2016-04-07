#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail():
    result = True         ###初始值为True
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
        msg['To'] = formataddr(["邪恶yi小人",'371725153@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("wptawy@126.com", "WW.3945.59")
        server.sendmail('wptawy@126.com', ['371725153@qq.com',], msg.as_string())
        server.quit()
    except Exception:
        result = False    ###捕捉到异常result值改为False
    return result       ###返回函数值


result = mail()      ####执行mail()函数并把return值赋值给result
if result:           ####对mail()函数返回值作判断
    print("发送成功")
else:
    print("发送失败")