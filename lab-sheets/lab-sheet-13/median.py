#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
    a.append(s)
    s = raw_input()

i = 0
j = i + 1
while i < len(a):
    p = i
    j = p + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1

        tmp = a[p]
        a[p] = a[i]
        a[p] = tmp

        i = i + 1
i = 0
while i < len(a):
    print a[i]
    i = i + 1
