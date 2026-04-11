'''
Bottom View of Binary Tree:
Given a binary tree, return an array of nodes visible from the bottom view from left to right.
Example 1:
Input:
       1
     /   \
    2     3
Output: 2 1 3
Example 2:
Input:
       1
     /   \
    2     3
     \     \
      4     5
Output: 2 4 3 5
Your Task:
You don't need to read input or print anything. Your task is to complete the function bottomView() which takes the root of the tree as input and returns an array of nodes visible from the bottom view from left to right.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105    


Solution approach:
1. We can use a breadth-first search (BFS) approach to traverse the binary tree level by level. We will maintain a queue to keep track of the nodes at each level and their corresponding horizontal distances from the root.
2. We will also maintain a dictionary to store the last node encountered at each horizontal distance. The horizontal distance of the root node is considered to be 0, the left child of the root node will have a horizontal distance of -1, the right child will have a horizontal distance of +1, and so on.
3. As we traverse the tree, we will check if the horizontal distance of the current node is already present in the dictionary. If it is not present, we will add the node's value to the dictionary with the horizontal distance as the key. If it is already present, we will update the value with the current node's value. This way, we will only store the last node encountered at each horizontal distance, which represents the bottom view of the tree.
4. After we have traversed the entire tree, we will sort the dictionary keys (horizontal distances) and create a list of the corresponding node values to return as the final result. This list will represent the nodes visible from the bottom view of the binary tree from left to right.

time complexity: O(N) where N is the number of nodes in the binary tree, as we need to visit each node once.
auxiliary space complexity: O(N) in the worst case, ifthe binary tree is skewed, we may need to store all nodes inthe queue andthe dictionary. Inthe best case, ifthe binary tree is balanced,the auxiliary space complexity would be O(log N) due tothe height ofthe tree. 

'''


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


from collections import deque


class Solution:
    def bottomView(self, root):
        # code here
        queue = deque()
        temp = {}
        res = []
        queue.append((root,0))
        
        while queue:
            node, line = queue.popleft()
            temp[line]=node.data
            if node.left:
                queue.append((node.left,line-1))
            if node.right:
                queue.append((node.right,line+1))
        
        for values in sorted(temp.items()):
            res.append(values[1])
        return res
        