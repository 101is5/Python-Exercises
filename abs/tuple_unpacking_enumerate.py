# TUPLE UNPACKING

# lists
l = [1,2,3,4]
a,b,c,d = l
 # a = 1, b = 2, c = 3, d = 4


# strings
s = 'assign'
t,u,v,x,y,z = s
 # t = 'a', u = 's', etc...

# ENUMERATE
    # Enumerate generates and unpacks tuples 
    # containing an index and its corresponding 
    # element, in that order.

    # Used in loops.

ls = [1,2,3,4,'5','a']
for i,j in enumerate(ls):
    print(f"index: {i}, element: {j}")
 # output: index: 0, element: 1
 #         ...
 #         index: 5, element: a

 # Note that the "a" is output unquoted
 # because it was printed.