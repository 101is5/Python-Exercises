from random import randint

def streak_count():
    count = 0
    flips = []
    for i in range(100):
        rand = randint(0,1)
        if rand:
            flips.append('H')
        else:
            flips.append('T')
    for i in range(len(flips)):
        streak = flips[i:i+6]
        if streak == ['H','H','H','H','H','H'] or streak == ['T','T','T','T','T','T']:
            count = 1
            break
    return count

streaks = 0
for x in range(10_000):
    streaks += streak_count()

percentage = streaks/100

print(f"Streaks of 6 heads or tails happened in {percentage}% of 10.000 coin flips.")