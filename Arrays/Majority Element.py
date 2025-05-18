"""
Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

Examples:

Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1
Explanation: Since, 1 is present more than 7/2 times, so it is the majority element.
Input: arr[] = [7]
Output: 7
Explanation: Since, 7 is single element and present more than 1/2 times, so it is the majority element.
Input: arr[] = [2, 13]
Output: -1
Explanation: Since, no element is present more than 2/2 times, so there is no majority element.
"""
# User function template for Python 3
from collections import Counter


class Solution:
    def majorityElement(self, arr):
        # code here
        n = len(arr) / 2
        dct = Counter(arr)
        for k, v in dct.items():
            if v > n:
                return k
        return -1


# {
# Driver Code Starts
# Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):
        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends