import re

ROMAN_VALUES = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

PATTERN = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'


def roman_numeral_to_int(roman):

    if not valid(roman):
        return None
    else:
        return convert(roman)


def convert(roman, remainder=''):

    if roman == '':
        return 0
    elif roman in ROMAN_VALUES:
        return ROMAN_VALUES[roman] + convert(remainder)
    else:
        remainder += roman[:1]
        return convert(roman[1:], remainder)


def valid(roman):

    if roman == '':
        return False
    if re.search(PATTERN, roman):
        return True
    else:
        return False


def main():
    print(roman_numeral_to_int('MMDCCCXCVI'))


if __name__ == '__main__':
    main()