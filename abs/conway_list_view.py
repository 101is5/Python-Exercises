# Get the index list for visualization
for i in range(6):
    print('[', end='')
    if i == 5:
        i = 'len(x)'
    for j in range(6):
        if j == 5:
            j = 'len(x)'
            print(f'x[{i}][{j}]', end='')
        else:
            print(f'x[{i}][{j}],', end=' ')    
    if i == j == 'len(x)':
        print(']')
    else:
        print('],')

x = [\
    [' ',' ',' ',' ',' ',' '],
    [' ',' ','#',' ',' ',' '],
    [' ',' ',' ','#',' ',' '],
    [' ','#','#','#',' ',' '],
    [' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ']
]

x_indexes = [x[0][0], x[0][1], x[0][2], x[0][3], x[0][4], x[0][len(x)]],
[x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], x[1][len(x)]],
[x[2][0], x[2][1], x[2][2], x[2][3], x[2][4], x[2][len(x)]],
[x[3][0], x[3][1], x[3][2], x[3][3], x[3][4], x[3][len(x)]],
[x[4][0], x[4][1], x[4][2], x[4][3], x[4][4], x[4][len(x)]],
[x[len(x)][0], x[len(x)][1], x[len(x)][2], x[len(x)][3], x[len(x)][4], x[len(x)][len(x)]]
