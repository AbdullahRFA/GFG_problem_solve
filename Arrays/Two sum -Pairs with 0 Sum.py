"""
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n)
"""
"""
✅ Algorithm (Step-by-step):
	1.	Use a set to store elements we’ve seen.
	2.	Use another set to store result pairs in tuple format to avoid duplicates.
	3.	For each number in the array:
        •	If its negation exists in the seen set, then:
        •	Add (min(num, -num), max(num, -num)) to the result set.
        •	Add the number to the seen set.
	4.	Convert the result set to a list of lists and sort the result before returning.
"""
#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        result = set()
        seen = set()
        for num in arr:
            if -num in seen:
                pair = (min(num,-num),max(num,-num))
                result.add(pair)
            seen.add(num)
        return sorted([list(pair) for pair in result])


#{
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.getPairs(arr)
        if len(res) == 0:
            print()
        else:
            IntMatrix().Print(res)
        print("~")
# } Driver Code Ends