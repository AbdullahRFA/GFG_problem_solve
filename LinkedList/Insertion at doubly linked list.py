"""
Given the head of a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list and return the head of the updated list.

Note: The position is 0-based indexed.

Examples:

Input:p = 2, x = 6

Output: 2 4 5 6
Explanation: Insert a node of value 6 after the 2nd node.

Input: p = 0, x = 44

Output: 1 44 2 3 4
Explanation: Insert a node of value 44 after the 0th node.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def addNode(self, head, p, x):
        # Code here
        current = head
        new_node = Node(x)

        i = 0
        while current and i < p:
            i += 1
            current = current.next

        new_node.prev = current
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node

        return head
