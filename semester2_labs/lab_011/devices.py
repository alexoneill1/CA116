#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        if line[0] == 'i':
            print('Dreadful and overpriced')
        else:
            print('Better Option')

if __name__ == '__main__':
    main()
