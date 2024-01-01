# given n, the number of non parallel lines   , the task is to find the maximum number of region in which the slice can divide the plane.

# Examples:
# n=3
# Output: 7

# n=2
# Output: 4


n=int(input())
print(n*(n+1)//2+1)