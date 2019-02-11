#!/usr/bin/env python

n = input()

i = 0
while i < n:
    if i % 2 == 0:
        print i
    else:
        print i * -1
    i = i + 1
