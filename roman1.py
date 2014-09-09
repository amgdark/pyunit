# -*- coding: utf8 -*-

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))


def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 4000):
        raise OutOfRangeError('numero fuera del rango (1-3999)')
    if not isinstance(n, int):
        raise NoIntegerError('Sólo numeros enteros')
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def from_roman(s):
    '''convert Roman numeral to integer'''
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result

class OutOfRangeError(ValueError):
    pass


class NoIntegerError(ValueError):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
