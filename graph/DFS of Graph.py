'''
DFS of Graph
Given a connected undirected graph. Perform a Depth First Traversal of the graph.
Example 1:
Input:  
Output: 0 1 2 3 4
Example 2:
Input:  
Output: 0 1 2 3 4
Your Task:
You don't need to read input or print anything. Your task is to complete the function dfs() which takes the adjacency list of the graph as input and returns the DFS traversal of the graph.
Expected Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph.
Expected Auxiliary Space: O(V) where V is the number of vertices in the graph.
Constraints:
1 ≤ Number of vertices ≤ 105
1 ≤ Number of edges ≤ 105
1 ≤ Data of a node ≤ 105    

Solution approach:DFS (Depth First Search) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. We can use a recursive approach to implement DFS. The algorithm starts at a given source vertex and explores as far as possible along each branch before backtracking. Here is the step-by-step approach to implement DFS for a graph:
1. Initialize a list to store the DFS traversal result and a visited list to keep track of the vertices that have already been visited to avoid processing the same vertex multiple times.
2. Define a recursive function that takes the current vertex, the result list, the visited list, and the adjacency list as parameters.
3. Mark the current vertex as visited and add it to the result list.
4. For each unvisited neighbor of the current vertex, recursively call the function with the neighbor as the new current vertex.
5. Continue this process until all reachable vertices have been processed.
6. Return the DFS traversal result list.


'''


class Solution:
     
    def dfs(self, adj):
        # code here
        
        res = []
        vis = [0]*len(adj)
        
        def solve(node,res,vis,adj):
            vis[node] = 1
            res.append(node)
            
            for x in adj[node]:
                if vis[x]==0:
                    solve(x, res, vis, adj)
        
        
        solve(0,res,vis,adj)
        
        return res