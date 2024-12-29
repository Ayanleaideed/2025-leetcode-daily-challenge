#Author: Ayanle 
#Data: Datetime.now()



'''
Problem Description:
The problem statement is an example of a graph-coloring problem where we want to color nodes (guests) with 2 colors such that no pair of connected nodes (pattern of dislikes) have the same color. If a proper coloring is possible, it will represent the valid seating arrangement. If not, it suggests controversy between attendees rendering any arrangement impossible.

Solution Approach:
The approach is to model this problem as a graph problem where each attendee is a node and each pair of non-matching attendees forms an edge. We will attempt to color this graph in two colors (0 and 1) and verifying that all edges connect the nodes of different colors - this is done by depth-first search (DFS).

Complexity Analysis:
- Time: O(N) as every attendee will be visited once during the DFS
- Space: O(N + D) where N is the number of attendees and D is the number of disliked pairs, as each of them will be stored in our adjacency list

'''

def optimizeGuestArrangement(N: int, dislikes: List[List[int]]) -> List[int]:

    # Initialize the color array with -1. -1 means not colored yet
    color_map = [-1] * (N + 1)
    # Represent dislikes as an adjacency list
    adj = collections.defaultdict(list)
    for u, v in dislikes:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node, color):
        color_map[node] = color
        for neighbor in adj[node]:
            if color_map[neighbor] == color:
                return False
            if color_map[neighbor] == -1 and not dfs(neighbor, 1 - color):
                return False
        return True

    # Start coloring each uncolored person
    for i in range(1, N + 1):
        if color_map[i] == -1 and not dfs(i, 0):
            return []
        
    # Return the optimized seating arrangement
    return [i for i in range(1, N + 1) if color_map[i] == 0] + [i for i in range(1, N + 1) if color_map[i] == 1]
