# print pattern 
# 1    5
#  2  4
#   3
#  2  2
# 1    1
# for i in range(5):
#     for j in range(5):
#         if i==j:
#             print(i+1,end="")
#         elif j==5-i-1:
#             print(j+1,end="")
#         else:
#             print(" ",end="")
#     print()

n = int(input())
p=1
q=n
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(q,end="")
            q-=1
        elif i==j :
            print(p,end="")
            p+=1
        else:
            print(" ",end="")
    print()
        