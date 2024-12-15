import re


def main():
    print(convert(input('Hours: ')))


def convert(s):
    if not validate(s):
        raise ValueError
    match validate(s):
        case 1:
            s = case_1(s)
            return s
        case 2:
            s = case_2(s)
            return s


def validate(s):
    # I think these are correct pattens, but they allow for 12 AM and 19 AM/PM
    # So I'll need to adjust cases for that
    if re.search(r'^1?[0-9] [A|P]M to 1?[0-9] [A|P]M$', s):
        return 1
    if re.search(r'^1?[0-9]:[0-5][0-9] [A|P]M to 1?[0-9]:[0-5][0-9] [A|P]M$', s):
        return 2
    return False


def case_1(s):
    # no minutes
    shift_start, shift_end = s.split(' to ')
    shift_start = shift_start.split(' ')
    shift_end = shift_end.split(' ')
    shift_start[0] = int(shift_start[0])
    shift_end[0] = int(shift_end[0])
    if shift_start[0] > 12 or shift_end[0] > 12:
        raise ValueError
    if 'AM' in shift_start[1] and shift_start[0] == 12:
        shift_start[0] = 0
    if 'AM' in shift_end[1] and shift_end[0] == 12:
        shift_end[0] = 0
    if 'PM' in shift_start[1] and shift_start[0] != 12:
        shift_start[0] += 12
    if 'PM' in shift_end[1] and shift_end[0] != 12:
        shift_end[0] += 12
    s = f'{shift_start[0]:02d}:00 to {shift_end[0]:02d}:00'
    return s

def case_2(s):
    # With minutes
    shift_start, shift_end = s.split(' to ')
    shift_start = shift_start.split(':')
    shift_end = shift_end.split(':')
    shift_start[0] = int(shift_start[0])
    shift_end[0] = int(shift_end[0])
    if shift_start[0] > 12 or shift_end[0] > 12:
        raise ValueError
    if 'AM' in shift_start[1] and shift_start[0] == 12:
        shift_start[0] = 0
    if 'AM' in shift_end[1] and shift_end[0] == 12:
        shift_end[0] = 0
    if 'PM' in shift_start[1] and shift_start[0] != 12:
        shift_start[0] += 12
    if 'PM' in shift_end[1] and shift_end[0] != 12:
        shift_end[0] += 12
    shift_start[1] = shift_start[1][:2]
    shift_end[1] = shift_end[1][:2]
    s = f'{shift_start[0]:02d}:{shift_start[1]} to {shift_end[0]:02d}:{shift_end[1]}'
    return s


if __name__ == '__main__':
    main()
