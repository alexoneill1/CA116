import sys

def main():
    for line in sys.stdin:
        [word, bigword] = line.lower().strip().split()

        if word in bigword:
            print(True)
        else:
            print(False)

if __name__ == '__main__':
    main()
