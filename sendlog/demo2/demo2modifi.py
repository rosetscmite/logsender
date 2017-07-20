#!/usr/bin/env python
# -*- codin: uth-8 -*-
# Author: jiaqiang_luo@hansight.com

import datetime
import re
import os

def demo2():
    nowtime = datetime.datetime.now()
    smtp_brutetime = nowtime.strftime("%FT%H:%M:%S")
    
    smtp_brutelog_str = ""

    smtp_brutelog = open('./log/smtp_brute.txt',"r")
    for line in smtp_brutelog:
        line = re.sub(r"\d+-\d+-\d+T\d+:\d+:\d+",smtp_brutetime,line)
        smtp_brutelog_str+=line
#    print smbscanlog_str
    newsmtp_brutelog = open('./log/smtp_brute.txt','w')
    newsmtp_brutelog.write(smtp_brutelog_str)
    smtp_brutelog.close()
    newsmtp_brutelog.close()


    print smtp_brutetime
if __name__ == '__main__':
    demo2()
