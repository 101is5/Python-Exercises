# Tic Tac Toe

# Implement single keystroke play: no need to press enter
# Todo: make a GUI (real game)

print("Pick a position to play(type a number from 1 to 9 and hit enter)\n")
numboard = [
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    [' ', 1 ,' ','|',' ', 2 ,' ','|',' ', 3 ,' ',],
    ['_','_','_','|','_','_','_','|','_','_','_',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    [' ', 4 ,' ','|',' ', 5 ,' ','|',' ', 6 ,' ',],
    ['_','_','_','|','_','_','_','|','_','_','_',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    [' ', 7 ,' ','|',' ', 8 ,' ','|',' ', 9 ,' ',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',]
]

board = [
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    ['_','_','_','|','_','_','_','|','_','_','_',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    ['_','_','_','|','_','_','_','|','_','_','_',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',],
    [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',]
]

playcount = 0
game = True
played = []     # positions taken

for i in numboard:
    for j in i:
        print(j, end='')
    print()

print()

for i in board:
    for j in i:
        print(j, end='')
    print()

start = input("Start game? ('yes or no')")
while start not in ['yes','no']:
    print("Invalid answer. Type either 'yes' or 'no: '")
    start = input()
if start == 'no':
    print('Bye!')
    game = False

while game:
    for i in ['x','o']:
        for x in board:
            for y in x:
                print(y, end='')
            print()
        
        position = int(input(f'Input position for {i} '))
        
        while position in played:
            print('Choose blank position\n')
            position = int(input(f'Input position for {i} '))
        
        match position:
            case 1:
                board[1][1] = i
            case 2:
                board[1][5] = i
            case 3:
                board[1][9] = i
            case 4:
                board[4][1] = i
            case 5:
                board[4][5] = i
            case 6:
                board[4][9] = i
            case 7:
                board[7][1] = i
            case 8:
                board[7][5] = i
            case 9:
                board[7][9] = i
                
        played.append(position)
        playcount += 1

        if \
            board[1][1] == board[1][5] == board[1][9] == i or \
            board[4][1] == board[4][5] == board[4][9] == i or \
            board[7][1] == board[7][5] == board[7][9] == i or \
            board[1][1] == board[4][1] == board[7][1] == i or \
            board[1][5] == board[4][5] == board[7][5] == i or \
            board[1][9] == board[4][9] == board[7][9] == i or \
            board[1][1] == board[4][5] == board[7][9] == i or \
            board[1][9] == board[4][5] == board[7][1] == i or \
            playcount == 9:
            print('game over')
            game = False
            break
