import sys

def main():
    i = 0
    nothing = 0
    one = 0
    two = 0
    three = 0
    str = 0
    flu = 0
    full = 0
    four = 0
    sf = 0
    rf = 0
    for line in sys.stdin:
        line = line.strip()
        if line[-1] == '0':
            nothing += 1
        elif line[-1] == '1':
            one += 1
        elif line[-1] == '2':
            two += 1
        elif line[-1] == '3':
            three += 1
        elif line[-1] == '4':
            str += 1
        elif line[-1] == '5':
            flu += 1
        elif line[-1] == '6':
            full += 1
        elif line[-1] == '7':
            four += 1
        elif line[-1] == '8':
            sf += 1
        elif line[-1] == '9':
            rf += 1

        i = i + 1

    print('The probability of nothing is ' + '{:.4f}'.format((nothing * 100) / i) + '%')
    print('The probability of one pair is ' + '{:.4f}%'.format((one / i) * 100))
    print('The probability of two pairs is ' + '{:.4f}%'.format((two / i) * 100))
    print('The probability of three of a kind is ' + '{:.4f}%'.format((three / i) * 100))
    print('The probability of a straight is ' + '{:.4f}%'.format((str / i) * 100))
    print('The probability of a flush is ' + '{:.4f}%'.format((flu / i) * 100))
    print('The probability of a full house is ' + '{:.4f}%'.format((full / i) * 100))
    print('The probability of four of a kind is ' + '{:.4f}%'.format((four / i) * 100))
    print('The probability of a straight flush is ' + '{:.4f}%'.format((sf / i) * 100))
    print('The probability of a royal flush is ' + '{:.4f}%'.format((rf / i) * 100))

if __name__ == '__main__':
    main()
