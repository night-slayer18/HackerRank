# Given a binary array A[] of size N. The task is to arrange the array in increasing order.
# Note: The binary array contains only 0  and 1.
 

# Example 1:

# Input: 
# 5
# 1 0 1 1 0

# Output: 
# 0 0 1 1 1

# Explanation: 
# After arranging the elements in 
# increasing order, elements will be as 
# 0 0 1 1 1.
# Example 2:

# Input:
# 10
# 1 0 1 1 1 1 1 0 0 0

# Output: 
# 0 0 0 0 1 1 1 1 1 1

# Explanation: 
# After arranging the elements in 
# increasing order, elements will be 
# 0 0 0 0 1 1 1 1 1 1.

# Your Task: This is a function problem. You only need to complete the function binSort() that takes the array A[] and it's size N as parameters and sorts the array. The printing is done automatically by the driver code.

# Expected Time Complexity: O(N)
# Expected Auxilliary Space: O(1)

# Constraints:
# 1 <= N <= 106
# 0 <= A[i] <= 1


# ***************************************************************************************************

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        #Your code here
        arr=[]
        for i in range(N):
            if A[i]==0:
                arr.append(0)
        for i in range(N):
            if A[i]==1:
                arr.append(1)
        for i in range(N):
            A[i]=arr[i]

N=int(input())
A=list(map(int,input().split()))
ob=Solution()
ob.binSort(A,N)
print(A)

# ***************************************************************************************************