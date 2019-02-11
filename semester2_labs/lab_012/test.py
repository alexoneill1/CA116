import sys

def foo():
    s = "Summer_Has_Arrived"

    try:
        print('A: {:s}'.format(s[::3]))
        print('A: {:s}'.format(s[-100:100]))
        i = len(s) // 5
        s[i].upper()
        print('C: {:s}'.fomrat(a[i]))
    except:
        print("Something Went Wrong!")

if __name__ == '__main__':
    foo()
