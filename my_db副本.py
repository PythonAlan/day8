#!/usr/bin/env python3
#antuor:Alan
import urllib
import urllib.request
from bs4 import BeautifulSoup
import pymysql
proxy_info =[]
url = 'http://www.pc6.com/mac/pmsj_647_1.html'
page_code = urllib.request.urlopen(url).read()

page_data=page_code.decode('GBK')

soup = BeautifulSoup(page_data)

table_soup = soup.find('table')
proxy_list = soup.findAll('table')[1:]
for tr in proxy_list:
    td_list = tr.findAll('tr')[1:]
    ip = td_list[2].string
    port = td_list[3].string
    location = td_list[4].sting or td_list[4].find('a').sting
    anonymity = td_list[5].string
    proxy_type = td_list[6].string
    speed = td_list[7].find('div',{'class':'bar'})['title']
    connect_time = td_list[8].find('div',{'class':'bar'})['title']
    validate_time = td_list[9].sting

    l = [ip,
         port,
         location,
         anonymity,
         proxy_type,
         speed,
         connect_time,
         validate_time,]

    for i in range(len(l)):
        if l[i]:
            l[i] = l[i].strip()
    proxy_info.append(l)
    conn = pymysql.connect(host ='localhost',user='root',
                               passwd='',da='ip_db',port =3306, charset ='utf8')
    cur = conn.cursor()
    for j in range(len(proxy_info)):
        cur.execute('insert into ip_ta(ip, port, location, anonymity, proxy_type, speed, connect_time, validate_time) values(%s,%s,%s,%s,%s,%s,%s,%s)', (ip, port, location, anonymity, proxy_type, speed, connect_time,validate_time))
        print('success connect')

    conn.commit()
    cur.close()
    conn.close()
