#!/usr/bin/env python
# -*- codin: uth-8 -*-
# Author: jiaqiang_luo@hansight.com

import datetime
import re
import os

def demo1():
    nowtime = datetime.datetime.now()
    fwtime = nowtime.strftime("%b %d %H:%M:%S")
    dir_brutetime1 = nowtime + datetime.timedelta(minutes=30)
    dir_brutetime = dir_brutetime1.strftime("%d/%b/%Y:%H:%M:%S")
    sqlinjecttime1 = dir_brutetime1 + datetime.timedelta(minutes=10)
    sqlinjecttime = sqlinjecttime1.strftime("%d/%b/%Y:%H:%M:%S")
    webshelltime1 = sqlinjecttime1 + datetime.timedelta(seconds=60)
    webshelltime = webshelltime1.strftime("%b %d %H:%M:%S")
    ftp_brutetime1 = webshelltime1 + datetime.timedelta(minutes=5)
    ftp_brutetime = ftp_brutetime1.strftime("%b %d %H:%M:%S")

    scanlog_str = ""
    dir_brutelog_str = ""
    sqlinjectlog_str = ""
    webshelllog_str = ""
    ftp_brutelog_str = ""

    scanlog = open('./log/scan.txt',"r")
    for line in scanlog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",fwtime,line)
        scanlog_str+=line
#    print smbscanlog_str
    newscanlog = open('./log/scan.txt','w')
    newscanlog.write(scanlog_str)
    scanlog.close()
    newscanlog.close()

    dir_brutelog = open('./log/dir_brute.txt','r')
    for line in dir_brutelog:
        line = re.sub(r"\d{1,2}/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2}",dir_brutetime,line)
        dir_brutelog_str+=line
#    print idslog_str
    newdir_brutelog = open('./log/dir_brute.txt','w')
    newdir_brutelog.write(dir_brutelog_str)
    dir_brutelog.close()
    newdir_brutelog.close()

    sqlinjectlog = open('./log/sqlinject.txt','r')
    for line in sqlinjectlog:
        line = re.sub(r"\d{1,2}/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2}",sqlinjecttime,line)
        sqlinjectlog_str+=line
#    print sysmonlog_str
    newsqlinjectlog = open('./log/sqlinject.txt','w')
    newsqlinjectlog.write(sqlinjectlog_str)
    sqlinjectlog.close()
    newsqlinjectlog.close()


    webshelllog = open('./log/webshell.txt',"r")
    for line in webshelllog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",webshelltime,line)
        webshelllog_str+=line
#    print smbscanlog_str
    newwebshelllog = open('./log/webshell.txt','w')
    newwebshelllog.write(webshelllog_str)
    webshelllog.close()
    newwebshelllog.close()


    ftp_brutelog = open('./log/ftp_brute.txt','r')
    for line in ftp_brutelog:
        line = re.sub(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",ftp_brutetime,line)
        ftp_brutelog_str+=line
#    print idslog_str
    newftp_brutelog = open('./log/ftp_brute.txt','w')
    newftp_brutelog.write(ftp_brutelog_str)
    ftp_brutelog.close()
    newftp_brutelog.close()

    print fwtime
    print dir_brutetime
    print sqlinjecttime
    print webshelltime
    print ftp_brutetime
if __name__ == '__main__':
    demo1()
