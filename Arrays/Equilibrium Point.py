"""
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists.

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.
"""


# User function Template for python3

class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            right_sum = total_sum - left_sum - arr[i]
            if left_sum == right_sum:
                return i
            left_sum += arr[i]

        return -1

    # pre = []
    # suf = []
    # for x in arr:
    #     pre.append(x)
    #     suf.append(x)
    #
    # for i in range(1, len(arr)):
    #     pre[i] += pre[i - 1]
    # print(pre)
    # for i in range(2, len(arr) + 1):
    #     suf[-i] += suf[-i + 1]
    #
    # print(suf)
    # for x in range(1, len(arr) - 1):
    #     if pre[x - 1] == suf[x + 1]:
    #         return x
    # return -1


# {
# Driver Code Starts
# Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends