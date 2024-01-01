#Asha’s birthday is shortly coming and her parents have planned to arrange for a houseparty. Deepa was Asha’s best friend and was expecting her birthday since a month. This isbecause Deepa’s Dad has promised her that he and Deepa together would design aReverse Talking kitty toy all by themselves and gift it to Asha.Deepa believed that Ashamight be overjoyed with this gift from her dear friend.Deepa’s Dad put the best of his efforts to design the toy. As a first module in the design heintended to write a program that would reverse a numeric input given to it. He needs yourhelp to write a recursive function for reversing the digits of the given number N. Please assist him in the task.Function Specifications: Use the function name, return type and the argument type as:int reverse(int) This recursive function should return the reverse of a N digit number. I/PFormat: The first line of the input an integer N. O/PFormat: Print the reverse of a N digit number.

# Input
# 1234

# Output

# 4321



# Solution

def reverse(n):
    if n<10:
        return n
    else:
        return str(n%10)+str(reverse(n//10))
    
n=int(input())

print(reverse(n))