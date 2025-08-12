"""
Given a doubly linked list. Your task is to reverse the doubly linked list and return its head.

Examples:

Input: LinkedList: 3 <-> 4 <-> 5
Output: 5 <-> 4 <-> 3

Input: LinkedList: 75 <-> 122 <-> 59 <-> 196
Output: 196 <-> 59 <-> 122 <-> 75

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= number of nodes <= 106
0 <= node->data <= 104
"""

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''


class Solution:
    def reverseDLL(self, head):
        # return head of reverse doubly linked list
        current = head
        temp = pre = None
        while current:
            temp = current.next
            current.next = pre
            current.prev = temp
            pre = current
            current = temp

        # current.
        # print(current.next.data)
        return pre
