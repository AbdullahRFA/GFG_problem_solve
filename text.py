#User function Template for python3
def fac(n):
    res = 1
    for x in range(2, n + 1):
        res *= x
    return res
class Solution:

    def nCr(self, n, r):
        # code here
        if n<r:
            return 0
        elif r==0:
            return 1
        return (fac(n)//(fac(n-r)*fac(r)))


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends