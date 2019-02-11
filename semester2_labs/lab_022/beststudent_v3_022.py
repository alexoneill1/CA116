import sys

def main():
    students = sys.argv[1]
    hi_mark = -1
    try:
        with open(students, 'r') as f:
            for line in f:
                try:
                    [mark, name] = line.strip().split(' ', 1)
                    if int(mark) > hi_mark:
                        hi_mark = int(mark)
                        hi_name = name

                except ValueError:
                    print('Invalid mark ' + mark + ' encountered. Skipping.')

    except FileNotFoundError:
        print('File not found, please try again!')

    finally:
        print('Best student:', hi_name)
        print('Best mark:', int(hi_mark))

if __name__ == '__main__':
    main()
