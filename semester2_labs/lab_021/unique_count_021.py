import sys
import string

def main():
    s = sys.stdin.read().strip().lower().split()
    s = sorted(s)

    result = []
    for item in s:
        item = item.strip(string.punctuation)
        if item not in result:
            if item not in string.punctuation:
                result.append(item)
    print(len(result))
    print(string.punctuation)
if __name__ == '__main__':
    main()
