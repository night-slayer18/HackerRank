# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, Return the index of any one of its peak elements.
# Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 


# Example 1:

# Input: 
# N = 3
# arr[] = {1,2,3}
# Possible Answer: 2
# Generated Output: 1
# Explanation: index 2 is 3.
# It is the peak element as it is 
# greater than its neighbour 2.
# If 2 is returned then the generated output will be 1 else 0.
# Example 2:

# Input:
# N = 3
# arr[] = {3,4,2}
# Possible Answer: 1
# Output: 1
# Explanation: 4 (at index 1) is the 
# peak element as it is greater than 
# it's neighbor elements 3 and 2.
# If 1 is returned then the generated output will be 1 else 0.
 

# Your Task:
# You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size N as input parameters and return the index of any one of its peak elements.

# Can you solve the problem in expected time complexity?

 

# Expected Time Complexity: O(log N)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 ≤ N ≤ 105
# 1 ≤ A[] ≤ 106

#***************************************************************************************************

class Solution:   
    def peakElement(self,arr, n):
        # Code here
        return arr.index(max(arr))



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)

#**************************************************************************************