n, m = map(int, input().split())
a = []
for i in range(n):
   a.append(list(map(int, input().split())))
ans = 0
for i in range(n-2):
   for j in range(m):
       if a[i][j] == a[i + 1][j]:
           continue
       elif a[i + 1][j] == 1 and a[i + 2][j] == 1:
           ans += 1
print(ans)