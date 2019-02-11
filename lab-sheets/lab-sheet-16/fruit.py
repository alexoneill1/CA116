#!/usr/bin/env python

import sys

a = sys.stdin.read().split()

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
while i < len(a):
    if a[i] in fruit:
        print a[i]
    i = i + 1
