#!/usr/bin/python

import ConfigParser, os
import io
import re


MY_CNF = "./my.cnf"


config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(open(MY_CNF))

##print config.get("mysqld999", "port")

LLD_DATA={}



for i in config.sections():
    if not re.match(r'.*\d$', i):
        continue

    LLD_DATA[i] = {}
    LLD_DATA[i].update({'REGION':i})

    if config.has_option(i,'socket'):
        LLD_DATA[i].update({'MYSQL_AGENT_SOCK':config.get(i,'socket') })

    if config.has_option(i,'bind-address'):
        LLD_DATA[i].update({'MYSQL_AGENT_IP':config.get(i,'bind-address') })


'''
max_connections
'''





if __name__ == '__main__':
    print '{'
    print '\t"data": ['


    OUT = []

    for x in  LLD_DATA.keys():
        OUT_TMP = []
        for k, v in LLD_DATA[x].items():
            OUT_TMP.append("\t\t\t\"{#%s}\": \"%s\"" % (k,v) )
        OUT.append("\t\t{\n" + ',\n'.join(OUT_TMP) + "\n\t\t}" )


    print "\n\t\t,\n".join(OUT)




    print '\t]'
    print '}'









