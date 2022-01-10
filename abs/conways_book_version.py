
# **************************************************************************
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# [The MODULUS operator in programing languages]
#
# The modulo operator is used to calculate the remainder of a division.
# In a regular situation, an expression like 1%10 would lead to thinking
# its remainder would be 0, since 1/10==0,1, leaving no remainder.
# However, in programing languages, in the specific case of the dividend
# being less than the divisor, the remainder i.e. the result of a modulo
# is the dividend itself.

# A simplistic reason for this could be because computers operate division 
# through successive subtractions, so in a modulus operation where
# divident < divisor they're left "stuck" in multiplying the divisor by zero 
# and then subtracting zero from the dividend, thus leaving the dividend 
# itself as the remainder.

# Obs.: Although the modulo operation works as described above, simple 
# divisions in programing languages where dividend < divisor most likely
# evaluate -as it does in Python- to a float, meaning such division could 
# be in fact remainderless. 
# That being the case, one could say regular divisions "go all the way" 
# down to fractions(floats), whilst modulo(%) and floor divisions(//) 
# stop when dividend < divisor.

# [The MODULUS operator in Pyhton]

# If dividend < divisor, dividend % divisor == dividend.
# E.g.:
#   1 % 9999 == 1
#   59 % 60 == 59
#   9999 % 10000 == 9999
#   -1 % 1000 ==
#       JavaScript: -1
#       Python: 999

# Some languages treat % as remainder, which is not always the case in 
# Python. Python's modulus is the "clock" type, as shown below:
#       
#       mod(a,n) = a - {n * Floor(a/n)}
#
# Or even better:
#
#       a % n = a - (n * (a//n))
#
# Pay special attention to the floor division in this formula, which in 
# case it evaluates to a negative number, it floors towards negative 
# infinty, which might be confusing at first. E.g.:
#  1 / 10 =  0.1, so  1//10 floors  0.1 down to  0, 
# whilst
# -1 / 10 = -0.1, so -1//10 floors -0.1 down to -1 

# As long as dividend < divisor, the divisor in this formula is called a 
# "wrapper", wrappping the possible results in a range from 0 to the value
# of the divisor minus 1(e.g. range(60)), even with a negative dividend:
# in this case, the modulus evaluates to the positive counterpart of the 
# negative dividend.
# This is why 59 % 60 and -1 % 60 both evaluate to 59. Get this as a Python
# list, where -1 refers to the same position as 59, the last one before 
# reaching 60, which is the value of the divisor.

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# **************************************************************************


# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.