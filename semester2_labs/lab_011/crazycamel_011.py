import sys

def main():
    for line in sys.stdin:
        line = line[::-1].strip()
        line = line.title()
        line = line[::-1]

        print(line)

if __name__ == '__main__':
    main()
