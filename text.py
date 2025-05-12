# User function Template for python3

class Solution:
    # Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        pre = []
        suf = []
        for x in arr:
            pre.append(x)
            suf.append(x)

        for i in range(1, len(arr)):
            pre[i] += pre[i - 1]
        print(pre)
        for i in range(2, len(arr) + 1):
            suf[-i] += suf[-i + 1]

        print(suf)
        for x in range(1, len(arr) - 1):
            if pre[x - 1] == suf[x + 1]:
                return x
        return -1


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