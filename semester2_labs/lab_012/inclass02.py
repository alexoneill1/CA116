import sys

def showfile(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                try:
                    print(int(line.strip()))
                except ValueError:
                    continue
    except (FileNotFoundError, PermissionError):
        print('Could not find file {:s}'.format(filename))
    else:
        print('Everything went well')
    finally:
        print('Goodbye')

def main():
    showfile(sys.argv[1])

if __name__ == '__main__':
    main()
