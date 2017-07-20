#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: lo0o.xing@gmail.com

import socket
import time

class Facility:
    "Syslog facilities"
    KERN, USER, MAIL, DAEMON, AUTH, SYSLOG, \
    LPR, NEWS, UUCP, CRON, AUTHPRIV, FTP = range(12)

    LOCAL0, LOCAL1, LOCAL2, LOCAL3, \
    LOCAL4, LOCAL5, LOCAL6, LOCAL7 = range(16, 24)


class Level:
    "Syslog levels"
    EMERG, ALERT, CRIT, ERR, \
    WARNING, NOTICE, INFO, DEBUG = range(8)


class Syslog(object):
    def __init__(self, host='localhost', port=9293, facility=Facility.DAEMON):
        self.host = host
        self.port = port
        self.facility = facility
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message, level):
        "Send a syslog message to remote host using UDP."
        #data = "<%d>%s" % (level + self.facility * 8, message)
        data = "%s" % (message)
        self.socket.sendto(data, (self.host, self.port))

    def warn(self, message):
        "Send a syslog warning message."
        self.send(message, Level.WARNING)

    def notice(self, message):
        "Send a syslog notice message."
        self.send(message, Level.NOTICE)

    def error(self, message):
        "Send a syslog error message."
        self.send(message, Level.ERR)


if __name__ == '__main__':
    ep_address = "172.16.100.231"
    execfile('demo2modifi.py')
    for line in open('./log/smtp_brute.txt', 'r'):
        try:
            syslog = Syslog(host=ep_address, port=514)
            syslog.send(line, Level.ERR)
        except OSError, exc:
            if exc.errno == 55:
                print 'error 55'
                time.sleep(1)
            else:
                raise
    print "send over!"
#    syslog = Syslog(host='172.16.100.231', port=514)
#    syslog.send('''a="123"''', Level.ERR)
#    syslog.send('''a="aab"''', Level.ERR)
#    syslog.send('''a=""''', Level.ERR)
#    syslog.send('''a="123"''', Level.ERR)
