#!/usr/bin/env python

import sys
src = sys.argv

with open(sys.argv[1], "w") as f:
    f.write("Hello world.\n")
