"""
http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python
"""

# -*- coding: utf-8 -*-
import json

# Make it work for Python1 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}

# Write JSON file
with io.open('filenames/filenameJson.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ':'), ensure_ascii=True)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('filenames/filenameJson.json') as data_file:
    data_loaded = json.load(data_file)

print(  data_loaded)
print(data == data_loaded)