import sys

def moo():
    s = "Skippy_the_kangeroo"
    try:
        print('A: {:s}'.format(s[::-3]))
        print('B: {:s}'.format(s[100:-100]))
        i = len(s) // 4
        s[i] = s[i].upper()
        print('C: {:s}'.format(s))

    except:
        print('Something went wrong!')
