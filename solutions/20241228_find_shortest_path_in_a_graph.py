'''
Problem Description and Constraints: 

Given a graph, we have to find the shortest path from a particular starting point to all other nodes in graph.

Solution Approach:

We use Dijkstra's algorithm for finding the shortest path from one node to another in a graph. We first initialize
the distances to all nodes as infinity except for the starting point. We initialize the distance of the starting point
to 0. Then we start traversing the graph. For every visited node, we check all its adjacent nodes. We update the distance 
of the adjacent node, if the previous distance of the node is greater than the sum of distance of current node and weight 
of edge connecting the current node and the adjacent node.

Time Complexity: O(V^2) - Because for every vertex, we are looking at all other vertices.
Space Complexity: O(V) - As we keep track of distance for all vertices.

Example Usage: find_shortest_path(graph, 0)

where graph is a 2D list representing adjacency matrix and 0 is the starting point.
'''

def find_shortest_path(graph, start):
    N = len(graph)
    visited = [False]*N
    distance = [float('inf')]*N
    distance[start] = 0
    
    for _ in range(N-1):
        min_distance = float('inf')
        for i in range(N):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                next_node = i
        visited[next_node] = True
        for i in range(N):
            if (not visited[i] and graph[next_node][i]
                and distance[next_node] + graph[next_node][i] < distance[i]):
                distance[i] = distance[next_node] + graph[next_node][i]
                
    return distance