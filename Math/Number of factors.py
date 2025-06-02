"""
Find the number of factors for a given integer N.


Example 1:

Input:
N = 5
Output:
2
Explanation:
5 has 2 factors 1 and 5
Example 2:

Input:
N = 25
Output:
3
Explanation:
25 has 3 factors 1, 5, 25

Your Task:
You don't need to read input or print anything. Your task is to complete the function countFactors() which takes an integer N as input parameters and returns an integer, total number factor of N.


Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)
"""
#User function Template for python3
class Solution:
    def countFactors (self, N):
        factor = []
        for i in range(1,int(N**0.5)+1):
            if N%i == 0:
                factor.append(i)
                if N//i != i:
                    factor.append(N//i)
        return len(factor)