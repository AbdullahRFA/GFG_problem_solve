"""
You are given a Doubly Linked List and an integer x. Remove the node at position x (positions are 1-indexed) from the list, and return the head of the updated list.

Examples:

Input: LinkedList = 1 <-> 3 <-> 4, x = 3
Output: 1 <-> 3
Explanation: After deleting the node at position 3 (position starts from 1),the linked list will be now as 1 <--> 3.

Input: LinkedList = 1 <-> 5 <-> 2 <-> 9, x = 1
Output: 5 <-> 2 <-> 9
Explanation: After deleting the node at position 1, the linked list will now look like 5 <-> 2 <-> 9.
Constraints:
2 <= size of the linked list <= 106
1 <= x <= size of the linked list
1 <= node->data <= 104


"""


class Solution:
    def delete_node(self, head, x):
        # code here
        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head

        current = head
        i = 1
        while current and i < x:
            i += 1
            current = current.next
        # print(current.data)
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        # if current.next.next:
        #     current.next.next.prev = current
        return head