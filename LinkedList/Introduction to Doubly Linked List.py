"""
Geek is learning data structures and is familiar with linked lists, but he's curious about how to access the previous element in a linked list in the same way that we access the next element. His teacher explains doubly linked lists to him.

Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it.

Example 1:

Input:
n = 5
arr = [1,2,3,4,5]
Output:
1 2 3 4 5
Explanation: Linked list for the given array will be 1<->2<->3<->4<->5.
Example 2:

Input:
n = 1
arr = [1]
Output:
1
Explanation: Linked list for the given array will be 1.
Constraints:
1 <= n <= 105
1 <= arr[i] <= 100

Your Task:
You don't need to read input or print anything. Your task is to complete the function constructDLL() which takes arr[] as input parameters and returns the head of the Linked List.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
"""


# User function Template for python3


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.current = None

    def create_DLL(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.current = new_node

        else:
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node
        return self.head


class Solution:
    def constructDLL(self, arr):
        dll = DoubleLinkList()
        head = None
        for x in arr:
            head = dll.create_DLL(x)
        return head
