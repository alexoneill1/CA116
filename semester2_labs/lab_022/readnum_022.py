import sys

def main():
    for line in sys.stdin:
        try:
            print('Thank you for', int(line.strip()))
            sys.exit()
        except ValueError:
            print(line.strip(), 'is not a number')


if __name__ == '__main__':
    main()
