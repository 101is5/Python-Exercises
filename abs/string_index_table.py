"""
This program is a function that takes an iterable and displays 
a table of its indexes and elements.

E.g.:
stringIndex('testString')
index:  0   1   2   3   4   5   6   7   8   9
char:  't' 'e' 's' 't' 'S' 't' 'r' 'i' 'n' 'g'

"""

def stringIndex(iterable):
    if type(iterable) == str:
        print('index: ', end='')
        for i in range(len(iterable)):
            print(f' {i}  ',end='')
        print()
        print('char:  ', end='')
        for i in range(len(iterable)):
            print(f"'{iterable[i]}'"+(' '*len(str(i))),end='')
        print()

    else:
        print('index: ', end='')
        for i in range(len(iterable)):
            print(f'{i}'+(' '*len(str(iterable[i]))),end='')
        print()
        print('items: ', end='')
        for i in range(len(iterable)):
            print(f'{iterable[i]}'+(' '*len(str(i))),end='')
        print()

stringIndex('stringona Imensa!')
stringIndex([1,2,3,4,5,6,7,8,9,10,11,12,111,1010,10101,11199,'a','b'])
stringIndex((1,2,3,4,5,6,7,8,9,10,11,12,111,1010,10101,12751894,'c','d'))