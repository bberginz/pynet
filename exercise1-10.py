#!/usr/bin/env python
'''
pynet week 1 exercise 10:
find crypto maps NOT using aes and print the transform set name
'''

from ciscoconfparse import CiscoConfParse

cisco_conf = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cisco_conf.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"transform-set AES")

print "Crypto maps not using AES:"

for c in crypto_map:
    print c.text
