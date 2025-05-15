"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
"""
⚙️ How It Works:

The algorithm uses three pointers:
	•	low: Points to the boundary of the 0s region.
	•	mid: Traverses the array and checks elements.
	•	high: Points to the boundary of the 2s region.

🔁 Logic:
	•	If arr[mid] == 0: Swap with arr[low], increment both low and mid.
	•	If arr[mid] == 1: Just move mid forward.
	•	If arr[mid] == 2: Swap with arr[high], decrement high (don’t increment mid yet!).
"""


# {
# Driver Code Starts

# } Driver Code Ends

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        n = len(arr) - 1
        low, mid, high = 0, 0, n
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1


# {
# Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends