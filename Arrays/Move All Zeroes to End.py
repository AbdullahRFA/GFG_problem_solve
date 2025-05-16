"""
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s
"""
"""
✅ Intuition:
	•	You iterate through the array using one pointer (i).
	•	Keep another pointer (j) that keeps track of the position to write the next non-zero element.
	•	When a non-zero is found at index i, place it at index j, and increment j.
	•	After the loop, all the non-zero elements are in place from 0 to j-1. So now, fill the rest of the array from j to end with zeros.
"""
#User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        for i in range(j, len(arr)):
            arr[i] = 0





#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends