# Coin Streak

# METHOD
# flip a coin 100 times
# make a list of the results
# check if streak
# repeat 10.000
# calculate streak percentage 

# LOGIC
# coin flip -> randint
# len(flips)=100
# streak check:
    # convert to string? (probably more concise)
        # convert whole list to string
        # check if 'hhhhhh' or 'tttttt' in string
    # count?
        # pick [i:i+5] slice
        # count h's and t's
        # if one counts 6, streak check


from random import randint

# string
streaks = 0
for x in range(10_000):
    string = ''
    for i in range(100):
        rand = randint(0,1)
        if rand:
            string += 'H'
        else:
            string += 'T'
    if 6*'H' in string or 6*'T' in string:
        streaks += 1

print(streaks/100)

# list
# streaks = 0
# for x in range(5):
#     flips = []
#     for i in range(20):
#         rand = randint(0,1)
#         if rand:
#             flips.append('H')
#         else:
#             flips.append('T')
#     for i in range(len(flips)):
#         slc = flips[i:i+6]
#         if slc == ['H','H','H','H','H','H'] or \
#             slc == ['T','T','T','T','T','T']:
#             streaks += 1
#             break

# print(streaks/100)
