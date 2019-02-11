#!/usr/bin/env python

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
    if files[i][-3:] == ".py":       # Line B.
        with open(files[i]) as f:
            if f.readline() == "#!/usr/bin/env python":
                print files[i]
    i = i + 1
