import sys

def main():
    for line in sys.stdin:
        [num, base] = line.strip().split()

        print(int(num, int(base)))

if __name__ == '__main__':
    main()
