'''
Problem Description:
Given a non-empty 2D grid containing three types of values (empty cells, coins and walls represented by 0, 1 and -1 respectively) and a starting point, we need to determine the maximum number of coins that can be collected by moving right and down, without moving into walls or outside the grid.

Solution Approach:
This problem can be solved using dynamic programming. The approach will be to start by initializing a DP table of the same size as the grid with all values set to 0. Then starting from the bottom right corner of the grid, for each cell we calculate the maximum coins that can be collected by moving to the right or down provided the cell is not a wall.

If the cell to the right or down is within the grid and not a wall, we will add the value of the current cell to the max DP value of the cell to the right and the cell below, and store the max of these values in the DP table. 

Finally, we will return the value in the DP table at the given starting point (this contains the maximum number of coins that can be collected from the starting point to the end of the grid).

Complexity Analysis:
- Time: O(m*n) where m and n are the dimensions of the grid. We have to iterate over every cell in the grid once.
- Space: O(m*n) for the space required to store the DP table.
'''

def solution_function(grid, start):
    """
    Takes a 2D grid and starting point, and returns the maximum number of coins that can be collected.
    Args: 
    grid: List of List of ints: 2D grid containg empty cells, coins and walls represented by 0, 1 and -1 respectively.
    start: Tuple of two ints: Starting point where the coin collection begins.

    Returns: 
    Int: The maximum number of coins that can be collected.
    """
    
    # Initialize a DP table
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Starting from the bottom-right corner
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):
            # If it's wall, skip
            if grid[i][j] == -1: continue
                
            # Calculate maximum coins can be collected by moving right or down
            right = dp[i][j + 1] if j + 1 < len(grid[0]) and grid[i][j + 1] != -1 else 0
            down = dp[i + 1][j] if i + 1 < len(grid) and grid[i + 1][j] != -1 else 0
                
            dp[i][j] = grid[i][j] + max(right, down)
        
    return dp[start[0]][start[1]]