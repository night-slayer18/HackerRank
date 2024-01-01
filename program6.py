n = input()
c=""
for i in n:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        c+=i*2
    else:
        c+=i
print(c)

    