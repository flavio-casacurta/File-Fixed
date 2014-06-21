=================================
 File Fixed - parser and unparser
=================================

Treating fixed format files

Overview
========

Arose a need to handle files with fixed data formats

As this need involve several types of records I decided to do a generic parse and  unparse

To set it up you need to create a JSON file with the following attributes:

- field    - field name
- type     - str or int
- length   - field length
- decimals - if decimals else zero

To use
======

from fixed_files import Fixed_files

ff = Fixed_files('record') # record.json

records = open('record.txt').readlines()

rec_in = []
for record in records:
     rec_in.append(ff.parse(record))

for n, r in enumerate(rec_in):
     print ff.unparse(r) + '\n' == records[n]



