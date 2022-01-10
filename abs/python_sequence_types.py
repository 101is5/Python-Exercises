# *******SEQUENCE TYPES*******

# Sequence types in Python are:

# **Mutable**
# 
# List
[1,2,3,4]
# Operations do not alter a list, but METHODS do. E.g.:
l = [1,2] + [3] # --> result == [1,2,3], but l remains [1,2]
l.append(3)     # --> l is now [1,2,3]

# **Immutable**
#
# String
'Sample'
"Another sample"
'this string ' + 'this other string'
"string" * 5
('string inside parentheses')
#
# Tuple
# Obs.: A unitary tuple must contain a trailing comma,
# or else it's another value inside parentheses
(1,2,3,4)
1,2,3,4
5,6,                # Trailing comma
('a','b',) * 10
(1,'a') + (2,'b',)
#
# Range objects
range(11)
range(1,1000)
range(3,55,2)
