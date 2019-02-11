 #!/usr/bin/env python

import sys

english_to_german = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn"
}

line = sys.stdin.readline()[:-1]
while line:
    print english_to_german[line]
    line = sys.stdin.readline()[:-1]
