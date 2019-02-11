#!/usr/bin/env python

a = input()
b = input()
c = input()

if a + b > c:
    if a + c > b:
        if b + c > a:
            print "yes"
else:
    print "no"
