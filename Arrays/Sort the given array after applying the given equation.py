"""
Given an integer array arr[] sorted in ascending order, along with three integers: A, B, and C. The task is to transform each element x in the array using the quadratic function A*(x2) + B*x + C. After applying this transformation to every element, return the modified array in sorted order.

Examples:

Input: arr[] = [-4, -2, 0, 2, 4], A = 1, B = 3, C = 5
Output: [3, 5, 9, 15, 33]
Explanation: After applying f(x) = 1*(x2)+ 3*x + 5 to each x, we get [9, 3, 5, 15, 33]. After sorting this array, the array becomes [3, 5, 9, 15, 33].
Input: arr[] = [-3, -1, 2, 4], A = -1, B = 0, C = 0
Output: [-16, -9, -4, -1]
Explanation: After applying f(x) = -1*(x2) + 0*x + 0 to each x, we get [ -9, -1, -4, -16 ]. After sorting this array, the array becomes  [-16, -9, -4, -1].
"""
class Solution:
	def sortArray(self, arr, A, B, C):
		# Code here
		for i in range(len(arr)):
		    arr[i] = A*arr[i]**2 + B*arr[i] + C
		return sorted(arr)


#{
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        a = int(input())
        b = int(input())
        c = int(input())

        ob = Solution()
        ans = ob.sortArray(arr, a, b, c)
        print(' '.join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends