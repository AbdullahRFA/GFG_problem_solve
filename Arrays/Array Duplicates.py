"""
Given an array arr of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3]
Explanation: 2 and 3 occur more than once in the given array.
Input: arr[] = [0, 3, 1, 2]
Output: []
Explanation: There is no repeating element in the array, so the output is empty.
Input: arr[] = [2]
Output: []
Explanation: There is single element in the array. Therefore output is empty.
"""

from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        # code here
        res = []
        if len(arr) == len(set(arr)):
            return res
        cnt = Counter(arr)
        for k,v in cnt.items():
            if v>1:
                res.append(k)
        return res



#{
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates
    # Sort the result in ascending order
    s.sort()
    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends