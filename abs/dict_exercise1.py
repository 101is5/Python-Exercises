# Convert list into dictionary turning neighbour elements
# (list[0] and list[0+1]) into key:value pairs

l = [i for i in range(1,21)]
# l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d = {}

for i in range(0,len(l),2):
    d[l[i]] = l[i+1]

# i = 0
# l[0] = 1 ; l[0+1] = 2
# d[l[0]] = l[0+1]
# d[1] = 2
# d = {1:2}

# i = 2
# l[2] = 3 ; l[2+1] = 4
# d[l[2]] = l[2+1]
# d[3] = 4
# d = {1:2,3:4}
