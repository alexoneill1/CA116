#!/usr/bin/env python

import sys

total = 0

with open(sys.argv[1]) as f:
    num = f.readline()
    while num:
        total = total + int(num)
        num = f.readline()

    print total
