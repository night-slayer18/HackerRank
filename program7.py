# the program will receive 3 english words from stdin. this 3 words will read one at a time , in three separate line. 
# the first word should be changed like all vowels should be replaced by * . 
# the second word should be changed like all consonants should be replaced by '@' . 
# the third word should be changed like all char should be converted to upper case. 
# then concatenate the three words and print them.

s1= input()
s2=input()
s3=input()
for i in s1:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        s1=s1.replace(i,'*')
for i in s2:
    if i not in ['a','e','i','o','u','A','E','I','O','U']:
        s2=s2.replace(i,'@')
s3=s3.upper()
print(s1+s2+s3)