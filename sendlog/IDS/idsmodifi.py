#!/usr/bin/env python
# -*- codin: uth-8 -*-
# Author: jiaqiang_luo@hansight.com

import time
import re
import os

def ids():
    idslog_str = ''
    millis = int(round(time.time() * 1000))
    newline = "timestamp\":"+str(millis)+",\"@end_timestamp\":"+str(millis)
    idslog = open('./idslog.txt',"r")
    for line in idslog:
        line = re.sub(r"timestamp\":\d+,\"@end_timestamp\":\d+",newline,line)
        idslog_str+=line
#    print smbscanlog_str
    newidslog = open('./idslog.txt','w')
    newidslog.write(idslog_str)
    idslog.close()
    newidslog.close()

def test():
    millis = int(round(time.time() * 1000))
    newline = "timestamp\":"+str(millis)+",\"\@end_timestamp\":"+str(millis)
    print newline

if __name__ == '__main__':
    ids()
