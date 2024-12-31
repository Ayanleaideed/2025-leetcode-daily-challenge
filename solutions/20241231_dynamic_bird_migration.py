'''
Problem Description:
The problem requires calculating the minimum migration time for a bird from the top-left corner of a NxN grid to the bottom-right cell. The bird can only move right or down from any given cell and has to rest exactly once in one of the provided rest cells.

Solution Approach:
We can use a dynamic programming approach, specifically a 2D DP table. We start from the initial position and make our way to the target position. For each position, we will check whether it is a rest cell, and calculate the minimal time taken so far, in order to get to that cell, from its neighbors i.e., from above or from left.

Complexity Analysis:
- Time: O(N^2 * M) where M is the number of rest cells. For each cell in the grid, we may need to process all rest cells.
- Space: O(N^2 * M) where N is the size of the grid and M is the number of rest cells to handle states of DP.
'''

def minimum_migration_time(N, rest_cells):
    """
    Function to calculate the minimal migration time for a bird moving through a grid, stopping to rest exactly once.
    Args: 
        N (int): size of the grid.
        rest_cells (list): list of tuple coordinates indicating rest cells.
    Returns: 
        (int): the minimum migration time.
    """
    # Initialize 3D dynamic programming table
    size = len(rest_cells)
    dp = [[[float('inf')] * size for _ in range(N)] for _ in range(N)]
    
    # Check if starting cell is a rest cell
    rest_cells = sorted(rest_cells)
    for i in range(size):
        if rest_cells[i] == (0,0):
            dp[0][0][i] = 1
        else:
            dp[0][0][i] = 0
    
    # Calculate minimal time for all cells
    for i in range(N):
        for j in range(N):
            for k in range(size):
                if (i, j) == rest_cells[k]: # If migratory bird is at rest cell
                    if i > 0:
                        dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k]+1)
                    if j > 0:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][k]+1)
                else:
                    if i > 0:
                        dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][l]+1 for l in range(size))
                    if j > 0:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][l]+1 for l in range(size))
    
    # If it's not possible to reach the destination, return -1
    if min(dp[N-1][N-1]) == float('inf'):
        return -1
    else:
        return min(dp[N-1][N-1])
