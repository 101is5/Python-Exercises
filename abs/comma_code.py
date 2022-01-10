# 'Comma code' turns a list into a string as if the list's elements
# are being read by a human: 
# ['sugar','spice','everything nice'] -> "sugar, spice and everything nice."

# There are three profiles to define:
# the first,
# the last, and
# the in betweens.
# Also the first profile can be the second-last's
# E.g.:

# 1) first element: 'element' (clean, no comma, no space), 
#    last:          ' and element.', 
#    in betweens:   ', element'.
#
# 2) from first to third-last: 'element, ',
#    second-last:              'element', (also clean)
#    last:                     ' and element.'

# For loops:
# Test: 1) for-looping through elements (for i in l)
#       2) for-looping through range (for i in range(len(l)))

# 1 (best one)
def comma_1(lst):
    string = ''
    l = list(lst)
    if l:
        if len(l) == 1:
            string += str(l[0]) + '.'
        else:
            for i in l:
                if i == l[0]:                           # first element
                    string += str(i)    
                elif i == l[len(l)-1]:                  # last element
                    string += ' and ' + str(i) + '.'
                else:                                   # in betweens
                    string += ',' + ' ' + str(i)
        return string
    else:
        return ''

# 2
def comma_2(lst):
    string = ''
    l = list(lst)
    if l:
        if len(l) == 1:
            string += str(l[0]) + '.'
        else:
            for i in range(len(l)):
                if not i:
                    string += str(l[i])
                elif i == len(l)-1:
                    string += ' and ' + str(l[i]) + '.'
                else:
                    string += ','  + ' ' + str(l[i])
        return string

# 3 Switching first's profile to second_last
def comma_3(lst):
    string = ''
    l = list(lst)
    if not l:
        return ''
    for i in l:
        if   i == l[len(l)-2]:               # second-last
            string += str(i)
        elif i == l[len(l)-1]:
            string += ' and ' + str(i) + '.' # last
        else:
            string += str(i)+','+' '         # from first to third-last
    return string