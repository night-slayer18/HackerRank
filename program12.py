# consider the following series 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187
# this series is a mixture of 2 series all the odd terms in the series form a geometric series and all the even terms form yet another geometric series write a program to find the nth term in the series
# write a program to find the nth term in the series

# test cases 
# input 1
# 5
# output 1
# 4

# input 2
# 6
# output 2
# 9

n= int(input())
if n%2==0:
    print(3**(n//2-1))
else:
    print(2**(n//2))