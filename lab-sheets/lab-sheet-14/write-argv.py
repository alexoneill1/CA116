!/usr/bin/env python

import sys
src = sys.argv
i = 0

with open("hello.txt", "w") as f:
    while i < len(sys.argv):
        f.write(sys.argv[i])
        i = i + 1
