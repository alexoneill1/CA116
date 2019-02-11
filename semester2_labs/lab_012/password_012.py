import sys

def counter(s):
    count = [0, 0, 0, 0]
    for c in s:
        if c.isdigit():
            count[0] = 1
        if c.isupper():
            count[1] = 1
        if c.islower():
            count[2] = 1
        if not(c.isalnum()):
            count[3] = 1
    return sum(count)

def main():
    for line in sys.stdin:
        print(counter(line.strip()))
if __name__ == '__main__':
    main()
