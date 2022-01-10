# Turn 90° to the right and print
# The order will go as grid[len(grid)-j][i], where
#   i is the outer loop variable, so it prints the column instead of the line, and
#   j is the inner loop variable, which goes up the column.
#   i starts at 0
#   j starts at 1
# E.g.: 9x6 list
#   grid[len(grid)-j][i]
#   First iteration:    grid[9-1][0]
#   Second iteration:   grid[9-2][0]...
#   Tenth iteration:    grid[9-1][1]
#   Eleventh iteration: grid[9-2][1]...
#   Last iteration:     grid[9-9][5]

# The challenge is to make it modular:
#   the unusual logic of the loops in this case is that the outer loop
#   has to reference the inner lists, and the inner loop the outer list.
# Solution:
#   Since the images are squared, hence there are two measures only
#   (len(list) and len(list[any index])), just store them and then set
#   the loops up with those values.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def roll90(grid):
    x = len(grid)-1
    y = len(grid[0])
    for i in range(y):
        for j in range(x,-1,-1):
            print(f"{grid[j][i]} ",end='')
        print()