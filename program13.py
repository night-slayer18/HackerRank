# Given two non-negative integers n1 and n2, where n1

# For example:

# Suppose n1=11 and n2=15.

# There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.

# Input Format

# Get the Integer value of n1 and n2 from the user

# Constraints

# Nil

# Output Format

# Print the output

# Sample Input 0

# 11
# 15

# Sample Output 0

# 4


# Solution

n1=int(input())
n2=int(input())
count=0
for i in range(n1,n2+1):
    if len(set(str(i)))==len(str(i)):
        count+=1
print(count)