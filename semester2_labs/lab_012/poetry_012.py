import sys

def main():
    largest = 0
    poem = []
    for line in sys.stdin:
        l = line.strip()
        poem.append(l)
        if len(l) > largest:
            largest = len(l)
    for l in poem:
        print('{:^{}}'.format(l, largest))

if __name__ == '__main__':
    main()
