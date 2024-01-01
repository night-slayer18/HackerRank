# jack and jill are playing string game. jack has given jill two strings A and B. jill has to derive a string C from A ,
# by deleting elements from string A, such that string C does not contain any elements of string B.
# jill need help to do this task. she wants a prohram to do this task. can you help her? 

# Input Format:

# Input consists of two strings separated by a space.

# Output Format:

# Output consists of a string.


str1,str2 = input().split()
l1= list(str1)
l2= list(str2)
for i in l2:
    if i in l1:
        l1.remove(i)
print("".join(l1))