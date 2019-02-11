#!/usr/bin/env python

n = input()
m = input()

i = 0
while i < n:
    print m
    if m % 2 == 0:
        m = m / 2
    else:
        m = (m * 3) + 1
    i = i + 1
