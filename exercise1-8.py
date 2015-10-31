#!/usr/bin/env python
'''
pynet week 1 exercise 8
parse cisco config and print out its crypto maps and their children
'''

from ciscoconfparse import CiscoConfParse

cisco_conf = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cisco_conf.find_objects(r"^crypto map")

for index,c in enumerate(crypto_map):
    print "Children of crypto map " + str(index + 1)
    for child in c.children:
        print child.text
