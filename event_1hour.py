# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:50:31 2021

@author: ZIM
"""
data=open("event_1hour_Sanhe.cat","w+")
for month in range(5,6,1):
    month='%02d' %month
    for day in range(1,31,1):
        day='%02d' %day
        if month=='6' and day=='31':
            continue
        for hour in range(0,23,1):
            hour='%02d' %hour
            print('2021'+'/'+str(month)+'/'+str(day)+','+str(hour)+':'+'00:00'+' '+'41.00 101.00 10 1',file=data)
data.close()