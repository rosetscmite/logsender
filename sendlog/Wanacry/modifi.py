#!/usr/bin/env python
# -*- codin: uth-8 -*-
# Author: jiaqiang_luo@hansight.com

import datetime
import re
import os

def Wanacry():
    nowtime = datetime.datetime.now()
    fwtime = nowtime.strftime("%b %d %H:%M:%S %Y")
    idstime1 = nowtime + datetime.timedelta(minutes=30)
    idstime = idstime1.strftime("%b %d %H:%M:%S")
    sysmontime1 = idstime1 + datetime.timedelta(seconds=10)
    sysmontime = sysmontime1.strftime("%a %b %d %H:%M:%S %Y")
    inside_smbscantime1 = sysmontime1 + datetime.timedelta(seconds=60)
    inside_smbscantime = inside_smbscantime1.strftime("%b %d %H:%M:%S %Y")
    inside_idstime1 = inside_smbscantime1 + datetime.timedelta(minutes=5)
    inside_idstime = inside_idstime1.strftime("%b %d %H:%M:%S")
    inside_sysmontime1 = inside_idstime1 + datetime.timedelta(seconds=10)
    inside_sysmontime = inside_sysmontime1.strftime("%a %b %d %H:%M:%S %Y")
    inside_smbscan_wromtime1 = inside_sysmontime1 + datetime.timedelta(seconds=60)
    inside_smbscan_wromtime = inside_smbscan_wromtime1.strftime("%b %d %H:%M:%S %Y")
#    fwtime = time.strftime('%b %d %H:%M:%S %Y',time.localtime(time.time()))
#    idstime = time.strftime('%b %d %H:%M:%S',time.localtime(time.time()))
#    sysmontime = time.strftime('%a %b %d %H:%M:%S %Y',time.localtime(time.time()))
    smbscanlog_str = ""
    idslog_str = ""
    sysmonlog_str = ""
    inside_smbscanlog_str = ""
    inside_idslog_str = ""
    inside_sysmonlog_str = ""
    inside_smbscan_wromlog_str = ""

    smbscanlog = open('./log/smbscan.txt',"r")
    for line in smbscanlog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",fwtime,line)
        smbscanlog_str+=line
#    print smbscanlog_str
    newsmbscanlog = open('./log/smbscan.txt','w')
    newsmbscanlog.write(smbscanlog_str)
    smbscanlog.close()
    newsmbscanlog.close()

    idslog = open('./log/ids.txt','r')
    for line in idslog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",idstime,line)
        idslog_str+=line
#    print idslog_str
    newidslog = open('./log/ids.txt','w')
    newidslog.write(idslog_str)
    idslog.close()
    newidslog.close()

    sysmonlog = open('./log/sysmon.txt','r')
    for line in sysmonlog:
        line = re.sub(r"\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",sysmontime,line)
        sysmonlog_str+=line
#    print sysmonlog_str
    newsysmonlog = open('./log/sysmon.txt','w')
    newsysmonlog.write(sysmonlog_str)
    sysmonlog.close()
    newsysmonlog.close()


    inside_smbscanlog = open('./log/inside_smbscan.txt',"r")
    for line in inside_smbscanlog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",inside_smbscantime,line)
        inside_smbscanlog_str+=line
#    print smbscanlog_str
    newinside_smbscanlog = open('./log/inside_smbscan.txt','w')
    newinside_smbscanlog.write(inside_smbscanlog_str)
    inside_smbscanlog.close()
    newinside_smbscanlog.close()


    inside_idslog = open('./log/inside_ids.txt','r')
    for line in inside_idslog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",inside_idstime,line)
        inside_idslog_str+=line
#    print idslog_str
    newinside_idslog = open('./log/inside_ids.txt','w')
    newinside_idslog.write(inside_idslog_str)
    inside_idslog.close()
    newinside_idslog.close()

    inside_sysmonlog = open('./log/inside_sysmon.txt','r')
    for line in inside_sysmonlog:
        line = re.sub(r"\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",inside_sysmontime,line)
        inside_sysmonlog_str+=line
#    print sysmonlog_str
    newinside_sysmonlog = open('./log/inside_sysmon.txt','w')
    newinside_sysmonlog.write(inside_sysmonlog_str)
    inside_sysmonlog.close()
    newinside_sysmonlog.close()

    inside_smbscan_wromlog = open('./log/inside_smbscan_wrom.txt',"r")
    for line in inside_smbscan_wromlog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",inside_smbscan_wromtime,line)
        inside_smbscan_wromlog_str+=line
#    print smbscanlog_str
    newinside_smbscan_wromlog = open('./log/inside_smbscan_wrom.txt','w')
    newinside_smbscan_wromlog.write(inside_smbscan_wromlog_str)
    inside_smbscan_wromlog.close()
    newinside_smbscan_wromlog.close()

    print fwtime
    print idstime
    print sysmontime
    print inside_smbscantime
    print inside_idstime
    print inside_sysmontime
    print inside_smbscan_wromtime
if __name__ == '__main__':
    Wanacry()
