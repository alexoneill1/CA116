import sys

es_endings = ['ch', 'sh', 'x', 's', 'z', 'o']
vowels = ['a', 'e', 'i', 'o', 'u']
#defining plural function
def plural(s):
    if s[-2:] in es_endings or s[-1:] in es_endings:
        s = s + "es"
    elif s[-1] == "y" and s[-2] not in vowels:
        s = s[:-1] + "ies"
    elif s[-1:] == 'f':
        s = s[:-1] + 'ves'
    elif s[-2:] == 'fe':
        s = s[:-2] + 'ves'
    elif s[-1:] == 'o':
        s = s + 'es'
    else:
        s = s + 's'

    return s


def main():
    for line in sys.stdin:
        print(plural(line.strip()))

if __name__ == "__main__":
    main()
