#!/usr/bin/env python

import sys

total = 0

i = 1
while i < len(sys.argv):
    with open(sys.argv[i]) as f:
        num = f.readline()
        while num:
            total = total + int(num)
            num = f.readline()
    i = i + 1
print total
