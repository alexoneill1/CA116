import sys
import calendar

def bday(day):
    poem = ["Monday's child is fair of face.",
            "Tuesday's child is full of grace.",
            "Wednesday's child is full of woe.",
            "Thursday's child has far to go.",
            "Friday's child is loving and giving.",
            "Saturday's child works hard for a living.",
            "Sunday's child is fair and wise and good in every way."]

    return 'You were born on a {} and {}'.format(calendar.day_name[day], poem[day])
def main():
    d = int(sys.argv[1])
    m = int(sys.argv[2])
    y = int(sys.argv[3])

    day = calendar.weekday(y, m, d)

    print(bday(day))

if __name__ == '__main__':
    main()
