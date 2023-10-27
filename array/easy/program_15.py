# Given an array A of n positive numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 
# 3 
# Explanation:  
# equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2). 
# Example 2:

# Input:
# n = 1
# A[] = {1}
# Output: 
# 1
# Explanation:
# Since there's only element hence its only the equilibrium point.
# Your Task:
# The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium. 

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= n <= 105
# 1 <= A[i] <= 109

# ***************************************************************************************************

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        i=0
        j=N-1
        sum1=A[i]
        sum2=A[j]
        while i<j:
            if sum1<sum2:
                sum1+=A[i+1]
                i+=1
            else:
                sum2+=A[j-1]
                j-=1
        if sum1==sum2:
            return i+1
        else:
            return -1
        

def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1

if __name__ == "__main__":
    main()

#***************************************************************************************************