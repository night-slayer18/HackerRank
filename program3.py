n = int(input())
for i in range(n):
    stones = int(input())
    if stones % 5 == 0 or stones %5==2:
        print("NO")
    else:
        print("YES")
