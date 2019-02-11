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
    a[i] = tmp

    i = i + 1
print a

n = input()
i = 1
while i < len(a):
    v = a[i]
    p = i
    while 0 < p and v < a[p - 1]:
        a[p] = a[p - 1]
        p = p - 1
    a[i] = v
    i = i + 1

print n
