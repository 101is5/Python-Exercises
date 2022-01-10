l = [1,2,'a','b']
l1 = [3,1,5,2]
l2 = ['b','a','d','A','B']
# Removing items:
    # remove()  --> takes ELEMENT
    # pop()     --> takes INDEX
    # popitem() --> 

    # There's also del, which is not a method:
    # del            --> del listname[index]

    # E.g.:
l.remove('a')
l.pop()

# Sorting items:
    # sort()   --> takes kwargs 'reverse=True' and 'key=str.lower'
    
    # Obs.: Can't sort elements of different types

    # E.g.
l1.sort()
l2.sort(reverse=True)
l2.sort(key=str.lower)
    # the key=str.lower kwarg prevents capital A and B 
    # from coming before lowercase a.

# Reversing item order:
    # reverse()
    # E.g.:
l1.reverse()
