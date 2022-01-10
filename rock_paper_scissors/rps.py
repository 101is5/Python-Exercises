from random import randint
from getpass import getpass
from time import sleep

def announce():
    print("                 Rock!...")
    sleep(0.5)
    print("                 Paper!...")
    sleep(0.5)
    print("                Scissors!...")
    sleep(0.5)
    

def score(score1,score2,p1_name='',p2_name=''):
    if mode == 1:
        print(f"""************SCOREBOARD************
       [{p1_name} {score1} X {score2} {p2_name}]\n""")
    elif mode == 2:
        print(f"""************SCOREBOARD************
       [Player {score1} X PC {score2}]\n""")

def cases(a,b):
    match (a,b):
        case (1,1)|(2,2)|(3,3):
            print("\nTie!")
            return 0
        case (1,3)|(3,1):
            print("\nRock breaks scissors!\n")
            return 1
        case (1,2)|(2,1):
            print("\nPaper wraps rock!\n")
            return 2
        case (2,3)|(3,2):
            print("\nScissors cut paper!\n")
            return 3

try:
    print("""\n
                    Welcome to 
                *---------------------*
                  ROCK PAPER SCISSORS!
                *---------------------*
""")
    sleep(1)
    print("""Choose a game mode or type Ctrl+C anytime you want to leave!
(Press Enter)""")

    press_enter = input()

    pl_score = 0
    pc_or_p2_score = 0

    print("""Would you like to play against a friend or me(the computer)?
A friend ->  type 1 and hit Enter
Me ------->  type 2 and hit Enter\n""")
    mode = int(input())
    while mode not in [1,2]:
        print("This is not a valid mode! So... 1 or 2?")
        mode = int(input())

    if mode == 1:
        print("[x] Two Player Mode")
        sleep(1)
        p1_name = input("\nPlayer 1, what is your name?\n").title()
        p2_name = input("\nPlayer 2, what is your name?\n").title()
        print("Ok!")
        sleep(0.5)
        print("\n***Remember to NOT let you opponent see your pick!")
        sleep(0.5)
        print("***Type Ctrl+C anytime you wish to quit\n")
        sleep(0.5)
        print("Have fun!\n")
        sleep(1)
    elif mode == 2:
        print("[x] Single player mode")
        sleep(1)
        print("\nGood luck!")

    while mode == 1:
        p1 = int(getpass(f"""{p1_name.title()}, type the corresponding number to play:
and hit Enter\nRock:1\nPaper:2\nScissors:3\n"""))
        while p1 not in [1,2,3]:
            print("Invalid entry! Choose 1, 2 or 3!")
            p1 = int(input())
        p2 = int(getpass(f"""\n{p2_name.title()}, type the corresponding number to play:
and hit enter\nRock:1\nPaper:2\nScissors:3\n"""))
        while p2 not in [1,2,3]:
            print("Invalid entry! Choose 1, 2 or 3!")
            p2 = int(input())

        announce()
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
        print("\nType the corresponding number to play:\nRock:1\nPaper:2\nScissors:3\n")
        player = int(input())
        pc = randint(1,3)

        announce()
        win = cases(player,pc)
        if win == player:
            pl_score += 1
            print("Player wins!")
            score(pl_score,pc_or_p2_score)
        elif win == pc:
            pc_or_p2_score += 1
            print("Computer wins!")
            score(pl_score,pc_or_p2_score)
except KeyboardInterrupt:
    print("\n***Thank you for playing!***\n")