# there are n stairs a person standing at the bottom wants to climb stairs to reach the nth stair.
# a person can climb either 1 or 2 stairs at a time,the task it to find the number of ways to reach the nth stair.

# input:
# 4

# output:
# 5

# input:
# 5

# output:
# 8

def count(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count(n-1) + count(n-2)

n = int(input())
print(count(n))