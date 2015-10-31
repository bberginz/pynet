#!/usr/bin/env python
'''
pynet week 1 exercise 7:
read YAML and JSON file and pretty print contents
'''

import yaml
import json
from pprint import pprint as pp

with open('ex1-6.yml') as f:
    yaml_data = yaml.load(f)

with open('ex1-6.json') as f:
    json_data = json.load(f)

pp(yaml_data)
pp(json_data)

