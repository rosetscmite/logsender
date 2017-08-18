#!/usr/bin/env python
# -*- codin: uth-8 -*-
# Author: jiaqiang_luo@hansight.com

import datetime
import re
import os

def demo4():
    nowtime = datetime.datetime.now()
    htatime = nowtime.strftime("%a %b %d %H:%M:%S %Y")

    htalog_str = ""

    htalog = open('./log/hta.txt',"r")
    for line in htalog:
        line = re.sub(r"\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}",htatime,line)
        htalog_str+=line
#    print smbscanlog_str
    newhtalog = open('./log/hta.txt','w')
    newhtalog.write(htalog_str)
    htalog.close()
    newhtalog.close()


    print htatime
if __name__ == '__main__':
    demo4()
