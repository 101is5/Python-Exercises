from random import randint

def streak_count():
    count = 0
    string = ''
    for i in range(100):
        rand = randint(0,1)
        if rand:
            string += 'H'
        else:
            string += 'T'
    if 6*'H' in string or 6*'T' in string:
        count = 1
    return count

streaks = 0
for x in range(10_000):
    streaks += streak_count()

percentage = streaks/100

print(f"Streaks of 6 heads or tails happened in {percentage}% of 10.000 coin flips.")
