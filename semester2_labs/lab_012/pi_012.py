import sys
import math

def pimath(n):
    print('{:.{}f}'.format(math.pi, n))


def main():
    return pimath(int(sys.argv[1]))

if __name__ == '__main__':
    main()
