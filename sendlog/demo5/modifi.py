#!/usr/bin/env python
# -*- codin: uth-8 -*-
# Author: jiaqiang_luo@hansight.com

import datetime
import re
import os

def demo5():
    nowtime = datetime.datetime.now()
    webscantime = nowtime.strftime("%b %d %H:%M:%S %Y")
    waflogtime1 = nowtime + datetime.timedelta(seconds=60)
    waflogtime = waflogtime1.strftime("%F %T")
    viruslogtime1 = waflogtime1 + datetime.timedelta(seconds=120)
    viruslogtime = viruslogtime1.strftime("%F %T")
#    inside_smbscan_wromtime = inside_smbscan_wromtime1.strftime("%b %d %H:%M:%S %Y")
    webscanlog_str = ""
    waflog_str = ""
    viruslog_str = ""

    webscanlog = open('./log/webscan.txt',"r")
    for line in webscanlog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",webscantime,line)
        webscanlog_str+=line
#    print smbscanlog_str
    newwebscanlog = open('./log/webscan.txt','w')
    newwebscanlog.write(webscanlog_str)
    webscanlog.close()
    newwebscanlog.close()


    waflog = open('./log/waflog.txt',"r")
    for line in waflog:
        line = re.sub(r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}",waflogtime,line)
        waflog_str+=line
#    print smbscanlog_str
    newwaflog = open('./log/waflog.txt','w')
    newwaflog.write(waflog_str)
    waflog.close()
    newwaflog.close()

    viruslog = open('./log/viruslog.txt',"r")
    for line in viruslog:
        line = re.sub(r"\d{4}-\d\d-\d\d\s+\d\d:\d\d:\d\d",viruslogtime,line)
        viruslog_str+=line
#    print smbscanlog_str
    newviruslog = open('./log/viruslog.txt','w')
    newviruslog.write(viruslog_str)
    viruslog.close()
    newviruslog.close()


    print webscantime
    print waflogtime
    print viruslogtime
if __name__ == '__main__':
    demo5()
