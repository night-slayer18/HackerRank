# aman and jasbir are playing a game 'game of numbers'. 
# there are n numbers on the table.since two players are playing the game,they will make their moves alternatively.
# in a move a player can perform the following operation.
# a player will choose a number from the table and will replace it with one of its divisor.
# the divisor should be a positive proper divisor of the number and it should be different from the number.
# a number cannot be replaced by more than one divisor in one move.
# a player cannot put back a number on the table.
# the player who cannot make any move loses the game.

# aman will make the first move of the game.
# you will be given n integers that are on the table in the start of the game.
# you have to predict the winner of the game.
# if aman wins print 'aman' (without quotes) else print 'jasbir' (without quotes).

# input format:
# first line contains an integer n.
# second line contains n space separated integers.

# output format:
# print the name of the winner of the game.

# constraints:
# 1<=n<=100000
# 1<=a[i]<=1000000

# sample input:
# 1
# 6

# sample output:
# aman

# sample input:
# 2
# 18 6

# sample output:
# aman



n = int(input())
a = list(map(int,input().split()))
if len(a) == 1:
    print('aman')
else:
    res=0
    for i in range(n):
        res^=a[i]
    if res == 0:
        print('jasbir')
    else:
        print('aman')



