"""
Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].

Examples:

Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and smallest positive missing number is 1.
Input: arr[] = [1, 3, 3]
Output: [3, 2]
Explanation: Repeating number is 3 and smallest positive missing number is 2.
Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5.
"""
"""
⸻

✅ Steps to Solve the Problem:
	•	Step 1: Use Counter from collections to count the frequency of each number in the array.
	•	Step 2: Identify the number that appears twice (frequency == 2) — this is the duplicate.
	•	Step 3: Calculate the sum of the array and subtract the duplicate once to simulate the correct sum.
	•	Step 4: Calculate the expected sum of numbers from 1 to n using the formula:expected_sum = (n*(n+1))/2
	•	Step 5: The missing number is: expected_sum-exact_sum
	•	Step 6: Return [duplicate, missing]

⸻

"""
#User function Template for python3
from collections import Counter
class Solution:
    def findTwoElement( self,arr):
        # code here
        dct = Counter(arr)
        twice = 0
        n = len(arr)
        for k,v in dct.items():
            if v == 2:
                twice = k
        exact_sum = sum(arr)-twice
        expected_sum = (n*(n+1))/2
        return [twice, int(expected_sum-exact_sum)]



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends