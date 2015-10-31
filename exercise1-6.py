#!/usr/bin/env python
'''
pynet week 1 exercise 6:
create list and write it out as YAML and JSON
'''

import yaml
import json

my_list = range(8)
my_list.append('string')
my_list.append('another string')
my_list.append( {'ip_addr':'192.169.100.1'} )
my_list.append( {'attribs':range(5) })

with open('ex1-6.yml', 'w') as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open('ex1-6.json', 'w') as f:
    json.dump(my_list, f)

