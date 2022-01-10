from random import randint

def score(score1,score2,p1_name='',p2_name=''):
    if mode == 1:
        print(f"{p1_name} {score1} X {score2} {p2_name}")
    elif mode == 2:
        print(f"Player {score1} X PC {score2}")

def cases(a,b):
    match (a,b):
        case (1,1)|(2,2)|(3,3):
            print("Tie!")
            return 0
        case (1,3)|(3,1):
            print("Rock breaks scissors!")
            return 1
        case (1,2)|(2,1):
            print("Paper wraps rock!")
            return 2
        case (2,3)|(3,2):
            print("Scissors cut paper!")
            return 3


print("""\n********************************************
This is Rock, Paper, Scissors!
Choose a game mode and after each match, press any key to play again!""")

pl_score = 0
pc_or_p2_score = 0

print("""\nWould you like to play against a friend or me(the computer)?
- a friend -> type 1
- me -> type 2\n""")
mode = int(input())

if mode == 1:
    print("Player 1, what is your name?")
    p1_name = input()
    print("\nPlayer 2, what is your name?")
    p2_name = input()
    print("\n***Remember to NOT let you opponent see your pick!")
    print("***Type Ctrl+C anytime you wish to quit\n")
    print("Have fun!\n")


while mode == 1:
    print(f"{p1_name.title()}, type the corresponding number to play:\nRock:1\nPaper:2\nScissors:3\n")
    p1 = int(input())
    print(f"{p2_name.title()}, type the corresponding number to play:\nRock:1\nPaper:2\nScissors:3\n")
    p2 = int(input())

    win = cases(p1,p2)
    if win == p1:
        pl_score += 1
        print(f"{p1_name} wins!")
        score(pl_score,pc_or_p2_score,p1_name,p2_name)
    elif win == p2:
        pc_or_p2_score += 1
        print(f"{p2_name} wins!")
        score(pl_score,pc_or_p2_score,p1_name,p2_name)

while mode == 2:
    print("Good luck!\n")
    print("Type the corresponding number to play:\nRock:1\nPaper:2\nScissors:3\n")
    player = int(input())
    pc = randint(1,3)

    win = cases(player,pc)
    if win == player:
        pl_score += 1
        print("Player wins!")
        score(pl_score,pc_or_p2_score)
    elif win == pc:
        pc_or_p2_score += 1
        print("Computer wins!")
        score(pl_score,pc_or_p2_score)