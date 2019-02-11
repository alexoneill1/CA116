import sys

def main():
    topmark = 0
    topstu = ''
    name = ''

    with open(sys.argv[1], 'r') as f:
        for line in f:
            try:
                    details = line.split()
                    mark = int(details[0])
                    name = " ".join(details[1:])

                    if mark > topmark:
                        topmark = mark
                        topstu = name
                    elif mark == topmark:
                        topstu = topstu + ", " + name

            except ValueError:
                print('Invalid mark encountered. Skipping.')

            except FileNotFoundError:
                print('The file sys.argv[1] could not be opened')

        print('Best student(s):', topstu)
        print('Best mark:', topmark)


if __name__ == '__main__':
    main()
