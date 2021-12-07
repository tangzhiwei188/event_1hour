# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:50:31 2021

@author: ZIM
"""
data=open("event_1hour_Sanhe.cat","w+")
for month in range(5,7,1):
    month='%02d' %month
    for day in range(1,32,1):
        day='%02d' %day
        if str(month)=='02' and str(day)=='31' :
            continue
        if str(month)=='02' and str(day)=='30' :
            continue
        if str(month)=='04' and str(day)=='31' :
            continue
        if str(month)=='06' and str(day)=='31' :
            continue
        if str(month)=='09' and str(day)=='31' :
            continue
        if str(month)=='11' and str(day)=='31' :
            continue
        for hour in range(0,24,1):
            hour='%02d' %hour
            print('2021'+'/'+str(month)+'/'+str(day)+','+str(hour)+':'+'00:00'+' '+'41.00 101.00 10 1',file=data)
data.close()