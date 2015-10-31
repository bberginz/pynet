#!/usr/bin/env python
'''
pynet week 1 exercise 9
parse cisco config and find crypto maps using pfs g2
'''

from ciscoconfparse import CiscoConfParse

cisco_conf = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cisco_conf.find_objects_w_child(parentspec=r"^crypto map", childspec=r"pfs group2")

print "Crypto maps using pfs group2:"

for index,c in enumerate(crypto_map):
    print c.text
    for child in c.children:
        print child.text
