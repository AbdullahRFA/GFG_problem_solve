"""
Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

Examples :

Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5
Explanation: Frequency of 1 is 5.
Input: arr = [1, 2, 3, 3, 2, 1], x=2
Output: 2
Explanation: Frequency of 2 is 2.
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105
1 <= x <= 105
"""
"""
You're given an array (arr)
Return the frequency of element x in the given array
"""

"""
You're given an array (arr)
Return the frequency of element x in the given array
"""


# class Solution:
#     def findFrequency(self, arr, x):
#         fre = {}
#         for i in arr:
#             fre[i] = fre.get(i, 0) + 1
#         if x in fre:
#             return fre[x]
#         else:
#             return 0
from collections import Counter
class Solution:
    def findFrequency(self, arr, x):
        fre = Counter(arr)
        if x in fre:
            return fre[x]
        else:
            return 0
slv = Solution()
arr = [1, 1, 1, 1, 1]
x = 1
print(slv.findFrequency(arr,x))