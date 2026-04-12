'''
BFS of graph
Given a graph, perform Breadth First Search (BFS) on the graph and return the BFS traversal of the graph.
Example 1:
Input:
Output: 0 1 2 3 4
Example 2:
Input:
Output: 0 1 2 3 4
Your Task:
You don't need to read input or print anything. Your task is to complete the function bfs() which takes the adjacency list of the graph as input and returns the BFS traversal of the graph.
Expected Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph.
Expected Auxiliary Space: O(V) where V is the number of vertices in the graph.
Constraints:
1 ≤ Number of vertices ≤ 105
1 ≤ Number of edges ≤ 105
1 ≤ Data of a node ≤ 105

Solution approach:BFS (Breadth First Search) is a graph traversal algorithm that explores the graph level by level. We can use a queue data structure to implement BFS. The algorithm starts at a given source vertex and explores all its neighbors before moving on to the neighbors' neighbors. Here is the step-by-step approach to implement BFS for a graph:

1. Initialize a queue to keep track of the vertices to be explored and a list to store the BFS traversal result.
2. Create a visited list to keep track of the vertices that have already been visited to avoid processing the same vertex multiple times.
3. Enqueue the starting vertex (usually vertex 0) and mark it as visited.
4. While the queue is not empty, repeat the following steps:
   a. Dequeue a vertex from the queue and add it to the BFS traversal result list.
   b. For each unvisited neighbor of the dequeued vertex, enqueue the neighbor and mark it as visited.
5. Continue this process until the queue is empty, which means all reachable vertices have been processed.
6. Return the BFS traversal result list.


'''


from collections import deque


class Solution:
    def bfs(self, adj):
        # code here
        
        queue = deque()
        ans = []
        vis = [0]*len(adj)
        
        queue.append(0)
        
        while queue:
            node = queue.popleft()
            if vis[node] == 0:
                ans.append(node)
                vis[node] = 1
                
                for x in adj[node]:
                    queue.append(x)
                
        return ans