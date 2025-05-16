"""
Given an array of strings arr[]. Return the longest common prefix among each and every strings present in the array. If there's no prefix common in all the strings, return "".

Examples :

Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
Output: "gee"
Explanation: "gee" is the longest common prefix in all the given strings.
Input: arr[] = ["hello", "world"]
Output: ""
Explanation: There's no common prefix in the given strings.
"""
#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        res = ""
        arr.sort()
        print(arr)
        n = min(len(arr[0]),len(arr[-1]))
        for i in range(n):
            if arr[0][i] == arr[-1][i]:
                res += arr[0][i]
            else:
                return res
        return res


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        ans = ob.longestCommonPrefix(arr)

        if not ans:
            print("\"\"")
        else:
            print(ans)

# } Driver Code Ends