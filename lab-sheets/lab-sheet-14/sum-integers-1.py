#!/usr/bin/env python

import sys

total = 0

num = sys.stdin.readline()
while num:
    total = total + int(num)
    num = sys.stdin.readline()

print total
