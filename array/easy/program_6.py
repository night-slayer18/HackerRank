# Find the missing element from an ordered array arr[], consisting of N elements representing an Arithmetic Progression(AP).

# Note: There always exists an element which upon inserting into sequence forms Arithmetic progression. Boundary elements (first and last elements) are not missing.

# Example 1:

# Input:
# N = 6
# Arr[] = {2, 4, 8, 10, 12, 14}
# Output: 6
# Explanation: Actual AP should be 
# 2, 4, 6, 8, 10, 12, 14.

# Example 2:

# Input:
# N = 6
# Arr[] = {1, 6, 11, 16, 21, 31}
# Output: 26
# Explanation: Actual AP should be 
# 1, 6, 11, 16, 21, 26, 31.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function findMissing() which takes the array of integers arr[] and its size n as input parameters and returns an integer denoting the answer.
 

# Expected Time Complexity: O(logN)
# Expected Auxiliary Space: O(1)


# Constraints:
# 2 <= N <= 105
# 0 <= |Arr[i]| <= 107
# There will always be only one missing element.

# ***************************************************************************************************

class Solution:
    def findMissing(self, arr, n):
        # code here
        sumOg=((n+1)*(arr[0]+arr[-1]))//2
        sumarr=sum(arr)
        return sumOg-sumarr
    
n=int(input())
arr=list(map(int, input().strip().split()))
print(Solution().findMissing(arr, n))

# ***************************************************************************************************