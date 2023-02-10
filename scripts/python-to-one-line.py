#!/usr/bin/env python

import sys
from python_to_one_line.oneLine import convert_to_one_line

filename = sys.argv[1]
with open(filename, 'r') as f:
    code = f.read()

print(convert_to_one_line(code))
