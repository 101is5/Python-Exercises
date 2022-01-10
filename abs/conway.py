# My approach to Conway's Game of Life

###################################################################################
# Build a len = 6 list of 6 lists representing a 6x6 diagram
# Nested for loops to check neighbours
# # = live element, ' ' = dead element
# If a living element has 2 or 3 living neighbours it remains alive, else dies (' ')
# If a dead element has 3 living neighbours it lives('#'), else remains dead

# Logic goals:
    # mirror the seed: copy its content to another list
    # look at seed, change copy
    # iterate through each element
    # identify the neighbours and check for live or dead
    # replace the seed content with copy's: seed = new generation

    # OBS.:
    # making changes to the seed will not work: that way, each loop iteration
    # would run neighbours() with a different list.

# This is a representation of the neighbours of a cell that has neighbours
# in all directions: x[i][j], which is absent in a list of only neighbours.
# Adjusting its position: if i or j are 0, just remove the elements whose 
# index or subindex would evaluate negative.
# neighbours = [\
#     x[i-1][j-1], x[i-1][j], x[i-1][j+1],
#     x[i]  [j-1], x[i]  [j], x[i]  [j+1],
#     x[i+1][j-1], x[i+1][j], x[i+1][j+1]
# ]
# x[0][5]
# neighbours = [\
#     x[i-1][j-1], x[i-1][j], x[i-1][j+1],
#     x[i]  [j-1], x[5]  [0], x[i]  [len(x)],
#     x[i+1][j-1], x[i+1][j], x[i+1][j+1]
# ]

###################################################################################

# To-do: 
    # [x] implement seed input
    # [x] stop when stable/print something
    # [x] build random seed builder
        # inspired by the book (Automate the Boring stuff with Python) 
    # [ ] print one message for stabilizing and another for all ' '
    # [ ] ask to run again with same or new measures

# OBS.:
    # New seed builder accidentally achieved [bug -> feature]
    # Builds new seed from the stabilized one: not randomly
    # The explanation comment is in the code(line 195)
    # Forgetting to copy lists managed to generate new seed

###################################################################################


from time import sleep
from copy import deepcopy
from random import randint

def neighbours(x,i,j):
    """
    Returns the 'neighbours' and only the neighbours
    of an element in a nested list.
    A neighbour is an element which is above, below,
    beside or at any corner of a given element.
    x = list
    i = index
    j = subindex
    The element provided to the function (x[i][j])
    will not show in the returned list.
    """
    match i:
        case 0:
            match j:
                case 0:
                    neighbours = [\
                                  x[i]  [j+1],
                        x[i+1][j],x[i+1][j+1]
                    ]
                case j if j==len(x)-1:
                    neighbours = [\
                        x[i]  [j-1], 
                        x[i+1][j-1], x[i+1][j]
                    ]
                    pass
                case _:
                    neighbours = [\
                        x[i]  [j-1],          x[i]  [j+1],
                        x[i+1][j-1],x[i+1][j],x[i+1][j+1]
                    ]
        case i if i==len(x)-1:
            match j:
                case 0:
                    neighbours = [\
                        x[i-1][j], x[i-1][j+1],
                                   x[i]  [j+1]
                    ]
                case j if j==len(x)-1:
                    neighbours = [\
                        x[i-1][j-1], x[i-1][j],
                        x[i]  [j-1]
                    ]
                case _:
                    neighbours = [\
                        x[i-1][j-1], x[i-1][j], x[i-1][j+1],
                        x[i]  [j-1],            x[i]  [j+1],
                    ]
        case _:
            match j:
                case 0:    
                    neighbours = [\
                        x[i-1][j],x[i-1][j+1],
                                  x[i]  [j+1],
                        x[i+1][j],x[i+1][j+1]
                    ]
                case j if j==len(x)-1:
                    neighbours = [\
                        x[i-1][j-1], x[i-1][j],
                        x[i]  [j-1],
                        x[i+1][j-1], x[i+1][j],
                    ]
                case _:
                    neighbours = [\
                        x[i-1][j-1],x[i-1][j],x[i-1][j+1],
                        x[i]  [j-1],          x[i]  [j+1],
                        x[i+1][j-1],x[i+1][j],x[i+1][j+1]
                    ]
    return neighbours



print("""
        [CONWAY'S GAME OF LIFE]

'#' --> Living cell
' ' --> Dead cell

RULES:
If a living cell has 2 or 3 living neighbours, it remains alive, or else, dies;
if a dead cell has 3 living neighbours, it lives, or else, remains dead.
\n""")

seed = []
again = ''

while True:
    print("""
    Would you like to\n
    1) provide the measures of the seed (Type 1 and hit Enter), or;
    2) build your own seed from scratch? (Type 2 and hit Enter) [Requires basic Python skills]
    """)
    answer = int(input())
    match answer:
        case 1:
            print("(Type a positive integer and hit Enter)")
            rows = int(input("Rows: "))         # amount of lists
            columns = int(input("Columns: "))   # lenght of lists

            # Seed builder
            for i in range(rows):
                seed.append([])
                for j in range(columns):
                    match randint(0,1):
                        case 0:
                            seed[i].append('#')
                        case 1:
                            seed[i].append(' ')
            new_gen = deepcopy(seed)
            first_seed = deepcopy(seed)
            break
        case 2:
            print("""
            A seed is a nested python list which must be
            populated with either:
            - a space: ' ' (representing a dead cell) or
            - a hashtag: '#' (representing a living cell)
            """)
            seed = list(input())
            break
        case _:
            print('Invalid answer. Type either 1 or 2 and hit Enter.\n')
            continue


try:
    while True:
        if again == 'n':
            print('You have watched the circle of life. Goodbye.\n')
            break
        for i in range(len(seed)):
            for j in range(len(seed[i])):
                count_living = 0
                nbrs = neighbours(seed,i,j)
                count_living += nbrs.count('#')
                match seed[i][j]:
                    case '#':
                        if count_living not in [2,3]:
                            new_gen[i][j] = ' '
                    case ' ':
                        if count_living == 3:
                            new_gen[i][j] = '#'
        if new_gen == seed:
            print('This generation has stabilized\n')
            while True:
                again = input('Go again? Yes(y) or no(n)?')
                match again:
                    case 'y':
                        seed = deepcopy(first_seed)
                        # Unexpectedly, not copying the last generation (seed = deepcopy(new_gen))
                        # but the very first one (seed = deepcopy(first_seed)) into the seed ended 
                        # up creating a new seed:
                            # At restart(line 190), seed and new_gen are different, so the program
                            # looks at one and makes changes to the other: obvious bug. However, at 
                            # the else condition below, the copying starts happening, applying the 
                            # changes properly from this point on, all from a newly created seed 
                            # based on this bug (so NOT randomly, btw).
                        break
                    case 'n':
                        break
                    case _:
                        print("Sorry. Invalid answer.\n")
                        continue
        else:
            for i in new_gen:
                print(i)
            seed = deepcopy(new_gen)
            print('\n')
            sleep(0.5)
except KeyboardInterrupt:
    print('You have interrupted the circle of life.\n')
