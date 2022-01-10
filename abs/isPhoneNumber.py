def isPhoneNumber(a):
    # the length check first prevents 'string index out of range'
    return (len(a) == 12 and\
        (a[3] == '-' and a[7] == '-') and\
        ''.join(a.split('-')).isdecimal())
        
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# This loop won't cause the 'string index out range error'
# because of the string slice.
# This is a great advantage of string slices:
# they ignore being out of range.
# E.g.: string = 'abcdef'
# The string slice string[:30] simply returns the whole string. 
# Now, the slice string[29:30] returns an empty string.
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')