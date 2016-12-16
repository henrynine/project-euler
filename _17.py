ones_digits = {'0': 0,
               '1': 3,
               '2': 3,
               '3': 5,
               '4': 4,
               '5': 4,
               '6': 3,
               '7': 5,
               '8': 5,
               '9': 4,}

tens_digits = {'0': 0,
               '2': 6,#teens are different
               '3': 6,
               '4': 5,
               '5': 5,
               '6': 5,
               '7': 7,
               '8': 6,
               '9': 6}

teens = {'10': 3,
         '11': 6,
         '12': 6,
         '13': 8,
         '14': 8,
         '15': 7,
         '16': 7,
         '17': 9,
         '18': 8,
         '19': 8}

def count_digits(num):
    to_count = str(num)
    length = len(to_count)
    if length == 1:
        return ones_digits[to_count]
    if length == 2:
        if to_count[0] == '1':
            return teens[to_count]
        else:
            return tens_digits[to_count[0]] + ones_digits[to_count[1]]
    if length == 3:
        mod = 0
        if to_count[1:] == '00':
            mod = -3#account for no 'and'
        return ones_digits[to_count[0]] + (10+mod) + count_digits(to_count[1:])

    if length == 4:
        return 11

total = 0
for n in range(1, 1001):
    total += count_digits(n)
print(total)
