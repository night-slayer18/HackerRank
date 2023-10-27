# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.
# Example 2:

# Input: 
# N = 3
# arr[] = {0 1 0}
# Output:
# 0 0 1
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 <= N <= 10^6
# 0 <= A[i] <= 2

# ***************************************************************************************************

class Solution:
    def sort012(self,arr,n):
        # code here
        a=[]
        for i in range(n):
            if arr[i]==0:
                a.append(0)
        for i in range(n):
            if arr[i]==1:
                a.append(1)
        for i in range(n):
            if arr[i]==2:
                a.append(2)
        for i in range(n):
            arr[i]=a[i]

            
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

#*******************************************************************************************************