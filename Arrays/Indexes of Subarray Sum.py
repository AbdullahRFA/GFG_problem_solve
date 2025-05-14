# User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        left, right = 0, 0
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum == target:
                return left, right
            elif sum > target:
                sum -= arr[left]
                left += 1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends