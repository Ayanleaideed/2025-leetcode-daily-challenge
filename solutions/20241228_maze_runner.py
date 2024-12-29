'''
Problem Description:
This problem involves searching for the shortest path in a 2D grid. The grid is a maze, with accessible and blocked cells. The goal is to find the shortest path from the top left cell to the bottom right cell, moving only to adjacent cells (vertically and horizontally).

Solution Approach:
We need a way to keep track of shortest paths, making BFS (Breadth-First Search) a good match for this scenario since it explores all the neighbors of a node before moving onto the nodes at the next level. We will make use of a queue to process nodes in a BFS fashion, starting with source cell. For each cell we visit, we push its valid neighboring cells into the queue and continue the process until reaching the destination cell. If we exhaust all cells and cannot reach the destination, there is no valid path and we return -1.

Complexity Analysis:
- Time: O(n^2), where n is the length of the side of the square grid. In worst-case scenario, when there are no obstacles in the grid, we would need to process each cell once.
- Space: O(n^2), where n is the length of the side of the square grid. In the worst case, our queue might need to store all the cells.
'''

from typing import List
from collections import deque

def findShortestPath(maze: List[List[int]]) -> int:
    """
    Calculate the shortest path from the top-left to the bottom-right cell in a 2D maze.
    Args:
    maze (List[List[int]]): A 2D grid representing the maze, 0 represents a blocked cell and 1 represents a free cell.
    Returns:
    int: The length of the shortest path, or -1 if no path exists.
    """
    # Eight possible directions: Top, Right, Down, Left 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(maze)
    
    #Validity check
    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return -1

    # Create visited matrix and initialize it with False
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True # marking (0,0) as visited

    # Initialize the queue with the start location and number of steps taken
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, step = queue.popleft() # Pop the cell from the queue

        # If reached to end of maze
        if x == n - 1 and y == n - 1:
            return step + 1

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # check validity of new cell
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n and maze[new_x][new_y] == 1 and visited[new_x][new_y] == False:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, step + 1)) # add the cell to the queue

    return -1 # if no path exists.