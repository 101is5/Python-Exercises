# The methods values(), keys() and items() return "view objects", iterables  
# the look like a list of tuples preceded by the corresponding name
# (dict_keys, dict_values or dict_items).

    # Remember: the list() function takes a single argument and separates the
    #           elements of it before gathering them in a list. So, assuming this 
    #           element is a string, it means it will be broken into its 
    #           characters, each of them becoming a list element.
    #           This could cause a mistake in case you want to build a list out 
    #           of just the values or keys in a dictionary(again, assuming
    #           they are strings).
    #           The items() method, on the other hand, gets away with it since
    #           it returns tuples containing the strings, not strings alone.

# A few different approaches in building actual lists out of a view object:
    # l += list(i)
    # l.append(i)
    # l.append(list(i))
    # list(eggs.values())
    # list(eggs) == list(eggs.keys())

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
a = []
b = []
c = []
d = list(eggs.values())
e = list(eggs)          # eggs alone is default for eggs.keys()
f = list(eggs.keys())

for i in eggs.values():
    a += list(i)
    b.append(i)
    c.append(list(i))

    # a == ['Z', 'o', 'p', 'h', 'i', 'e', 'c', 'a', 't', '8']
    # b == ['Zophie', 'cat', '8']
    # c == [['Z', 'o', 'p', 'h', 'i', 'e'], ['c', 'a', 't'], ['8']]

    # The difference between a and c is:
    #     a) adding lists gathers all elements into a single list;
    #     b) a list is built and then appended to the list in b.

d = list(eggs.values())
# ['Zophie', 'cat', '8']
e = list(eggs)
# ['name','species','age']
f = list(eggs.keys())
# same as above

for i in eggs.items():
    a += list(i)
    b.append(i)
    c.append(list(i))

    # a == ['name', 'Zophie', 'species', 'cat', 'age', '8']
    # b == [('name', 'Zophie'), ('species', 'cat'), ('age', '8')]
    # c == [['name', 'Zophie'], ['species', 'cat'], ['age', '8']]

    # items()'s view object returns a list of tuples, so now:
    # a) each tuple becomes a list, then is added together in a 
    #   single final list;
    # b) tuples aren't converted at all and are successively appended
    #   to b, which ends up as a list of tuples
    # c) each tuple is converted into a list, which are successively
    #   appended to c, which ends up as nested list.

# Also, since items() returns tuples, tuple unpacking is possible:
for i,j in eggs.items():
    print(f"key: {i}, value: {j}")
    # Obs.: Now i and j are strings from the eggs dictionary, which 
    #   need attention not to be inadvertently converted into lists.

# The get() method offers a fallback value for inexistant keys.
# This inexistent key, though, will not be added to the dictionary.
eggs.get('color','green')

# The setdefault() method is a get() method that adds the inexistent 
# key:value pair to the dictionary.

