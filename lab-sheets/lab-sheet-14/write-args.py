#!/usr/bin/env python

import sys
src = sys.argv
i = 0

with open(sys.argv[1], "w") as f:
    while i < len(sys.argv):
        f.readline()
        i = i + 1
        print i
