#!/usr/bin/python

import ConfigParser, os
import io
import re


MY_CNF = "./my.cnf"


config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(open(MY_CNF))

##print config.get("mysqld999", "port")




for i in config.sections():
    if not re.match(r'.*\d$', i):
        continue


    print i





