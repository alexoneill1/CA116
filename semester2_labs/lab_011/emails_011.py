import sys

def main():
    for line in sys.stdin:
        line = line.strip().strip('@mail.dcu.ie')
        line = line.strip('0123456789')
        line = line.title()
        line = line.replace('.', ' ', 1)



        print(line)

if __name__ == '__main__':
    main()
