'''
Top View of Binary Tree:
Given a binary tree, return an array of nodes visible from the top view from left to right.
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
Output: 2 1 3 5
Your Task:
You don't need to read input or print anything. Your task is to complete the function topView() which takes the root of the tree as input and returns an array of nodes visible from the top view from left to right.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105    


Solution approach:
1. We can use a breadth-first search (BFS) approach to traverse the binary tree level by level. We will maintain a queue to keep track of the nodes at each level and their corresponding horizontal distances from the root.
2. We will also maintain a dictionary to store the first node encountered at each horizontal distance. The horizontal distance of the root node is considered to be 0, the left child of the root node will have a horizontal distance of -1, the right child will have a horizontal distance of +1, and so on.
3. As we traverse the tree, we will check if the horizontal distance of the current node is already present in the dictionary. If it is not present, we will add the node's value to the dictionary with the horizontal distance as the key. This way, we will only store the first node encountered at each horizontal distance, which represents the top view of the tree.
4. After we have traversed the entire tree, we will sort the dictionary keys (horizontal distances) and create a list of the corresponding node values to return as the final result. This list will represent the nodes visible from the top view of the binary tree from left to right.

time complexity: O(N) where N is the number of nodes in the binary tree, as we need to visit each node once.
auxiliary space complexity: O(N) in the worst case, if the binary tree is skewed, we may need to store all nodes in the queue and the dictionary. In the best case, if the binary tree is balanced, the auxiliary space complexity would be O(log N) due to the height of the tree. 
'''



class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def topView(self, root):
        # code here
        
        queue = deque()
        res = []
        temp = {}
        queue.append((root,0))
        
        while queue:
            node,line=queue.popleft()
            
            if line not in temp:
                temp[line]=node.data
            if node.left:
                queue.append((node.left,line-1))
            if node.right:
                queue.append((node.right,line+1))
        
        for values in sorted(temp.items()):
            res.append(values[1])
        return res
        

# Driver Code Starts
if __name__ == "__main__":
    # Constructing the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(5)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calling the topView function and printing the result
    result = solution.topView(root)
    print(result)  # Output: [2, 1, 3, 5]
# Driver Code Ends