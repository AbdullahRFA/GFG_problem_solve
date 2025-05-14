"""
Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.

Note: If multiple occurrences are there, please return the smallest index.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], k = 4
Output: 3
Explanation: 4 appears at index 3.
Input: arr[] = [11, 22, 33, 44, 55], k = 445
Output: -1
Explanation: 445 is not present.
Input: arr[] = [1, 1, 1, 1, 2], k = 1
Output: 0
Explanation: 1 appears at index 0.
Note: Try to solve this problem in constant space i.e O(1)
"""


class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        left = 0
        right = len(arr) - 1
        result = -1
        while left <= right:
            mid = int((left + right) / 2)
            if arr[mid] == k:
                result = mid
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return result


# {
# Driver Code Starts
# Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends