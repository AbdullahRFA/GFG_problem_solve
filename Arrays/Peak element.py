"""
Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples :

Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6].
Input: arr = [1, 2, 3]
Output: true
Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right.
"""


class Solution:
    def peakElement(self, arr):
        # Code here
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1
        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i
        return i


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends