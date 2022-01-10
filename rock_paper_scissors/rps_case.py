from random import randint

def rps(a,b):
    if a == b:
        print("It's a tie!")
        return 0
    match (a,b):
        case (1,3)|(3,1):
            print('Rock breaks scissors!')
            return 1
        case (1,2)|(2,1):
            print('Paper wraps rock!')
            return 2
        case (2,3)|(3,2):
            print('Scissors cut paper!')
            return 3

def play(p1,p2):
    p1 = int(input())
    p2 = int(input())
    return p1,p2

while True:
    class Player:
        player1 = int(input())
        player2 = int(input())
        win = int(rps(player1,player2))
    if Player.win == 0:
        continue
    match Player.win:
        case Player.player1:
            print("player 1 wins")
        case Player.player2:
            print("player 2 wins")