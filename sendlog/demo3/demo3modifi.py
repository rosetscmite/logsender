#!/usr/bin/env python
# -*- codin: uth-8 -*-
# Author: jiaqiang_luo@hansight.com

import datetime
import re
import os

def demo3():
    nowtime = datetime.datetime.now()
    usbtime = nowtime.strftime("%a %b %d %H:%M:%S %Y")
    rundlltime1 = nowtime + datetime.timedelta(minutes=5)
    rundlltime = rundlltime1.strftime("%a %b %d %H:%M:%S %Y")
    idstime1 = rundlltime1 + datetime.timedelta(minutes=5)
    idstime = idstime1.strftime("%b %d %H:%M:%S")

    usblog_str = ""
    rundlllog_str = ""
    idslog_str = ""

    usblog = open('./log/usb.txt',"r")
    for line in usblog:
        line = re.sub(r"\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",usbtime,line)
        usblog_str+=line
#    print smbscanlog_str
    newusblog = open('./log/usb.txt','w')
    newusblog.write(usblog_str)
    usblog.close()
    newusblog.close()

    rundlllog = open('./log/rundll.txt','r')
    for line in rundlllog:
        line = re.sub(r"\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",rundlltime,line)
        rundlllog_str+=line
#    print idslog_str
    newrundlllog = open('./log/rundll.txt','w')
    newrundlllog.write(rundlllog_str)
    rundlllog.close()
    newrundlllog.close()

    idslog = open('./log/ids.txt','r')
    for line in idslog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",idstime,line)
        idslog_str+=line
#    print sysmonlog_str
    newidslog = open('./log/ids.txt','w')
    newidslog.write(idslog_str)
    idslog.close()
    newidslog.close()


    print usbtime
    print rundlltime
    print idstime
if __name__ == '__main__':
    demo3()
