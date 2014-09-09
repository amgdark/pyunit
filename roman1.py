"""
>>> to_roman(4000)
'MMMM'
>>> to_roman(5000)
'MMMMM'
>>> to_roman(9000)
'MMMMMMMMM'
"""
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
    if not (0< n < 4000):
        raise OutOfRangeError('numero fuera del rango (1-3999)')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result+= numeral
            n -= integer
    return result

class OutOfRangeError(ValueError):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
