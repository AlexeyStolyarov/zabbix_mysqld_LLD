#!/usr/bin/python

import ConfigParser, os
import re

MY_CNF = "./my.cnf"
ADRESS_MATCH_MASK = "10.21"
DEFAULT_ADRESS = ""
DEFAULT_PORT_MYSQL = "3306"

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(open(MY_CNF))


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
    else:
        LLD_DATA[i].update({'MYSQL_AGENT_IP': DEFAULT_ADRESS })


    if config.has_option(i,'port'):
        LLD_DATA[i].update({'MYSQL_AGENT_PORT':config.get(i,'port') })
    else:
        LLD_DATA[i].update({'MYSQL_AGENT_PORT': DEFAULT_PORT_MYSQL })





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








