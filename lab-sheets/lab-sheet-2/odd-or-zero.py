#!/usr/bin/env python

n = input()

i = 0
while i < n and n % 2 == 0:
    print "0"
    while n % 2 != 0:
        print n
i = i + 1
