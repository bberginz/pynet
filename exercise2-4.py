#!/usr/bin/env python
'''
pynet week 2 exercise 4
using snmp_helper to connect to both rtr1 and rtr2 and print out the MIB2
sysName and sysDescr
'''

from snmp_helper import snmp_get_oid,snmp_extract

def print_oid_data(device, my_oid):
    snmp_data = snmp_get_oid(device, oid=my_oid)
    print snmp_extract(snmp_data)

COMMUNITY_STRING = 'galileo'
IP = '50.76.53.27'
SNMP_PORT_RTR1 = 7961
SNMP_PORT_RTR2 = 8061

SYSDESC_OID = '1.3.6.1.2.1.1.1.0'
SYSNAME_OID = '1.3.6.1.2.1.1.5.0'

rtr1_device = (IP, COMMUNITY_STRING, SNMP_PORT_RTR1)
rtr2_device = (IP, COMMUNITY_STRING, SNMP_PORT_RTR2)

print 'pynet-rtr1 sysName:'
print_oid_data(rtr1_device, SYSNAME_OID)
print 'pynet-rtr1 sysDescr:'
print_oid_data(rtr1_device, SYSDESC_OID)

print 'pynet-rtr2 sysName:'
print_oid_data(rtr2_device, SYSNAME_OID)
print 'pynet-rtr2 sysDescr:'
print_oid_data(rtr2_device, SYSDESC_OID)
