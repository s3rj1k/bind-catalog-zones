#!/usr/bin/env python

import dns.name
import hashlib
import sys
import os

zone_suffix_name = '.zone'

print('@ 3600 SOA . . 42 86400 3600 86400 3600')
print('@ 3600 IN NS nop.')
print('version IN TXT "1"')

for el in os.listdir(path='./zone'):
  if el.endswith(zone_suffix_name):
    el = el[:-len(zone_suffix_name)]
    hash = hashlib.sha1(dns.name.from_text(el).to_wire()).hexdigest()
    print('{}.zones\tPTR\t{}.'.format(hash, el))
