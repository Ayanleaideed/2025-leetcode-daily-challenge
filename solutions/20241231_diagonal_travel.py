'''
Problem Description:
Given a two-dimensional grid of integers, write a function that starts at the top-left corner of the grid and moves towards the bottom-right corner. The traversal can only be right, down or diagonally right-down. The function should return the sum of every integer visited during the traversal.

Solution Approach:
We begin by initializing a matrix with the same size as the input grid and fill it with zeros. The element at the (i, j) position of the matrix will represent the maximum path sum to reach the element at position (i, j) in the grid.
The initial value matrix[0][0] is equal to grid[0][0] as we start from the top left of the grid.
We compute the other elements of the first row and first column as they can be only visited from left element (for first row) and top element (for first column) respectively.
We then compute the rest of the matrix, where the element at the (i, j) position of the matrix represents the maximum of matrix[i-1][j-1] (diagonal), matrix[i][j-1] (left) and matrix[i-1][j] (top) plus the matching element from the grid.
The value matrix[n-1][m-1] will be the maximum path sum that we can reach.

Complexity Analysis:
- Time: O(n*m) as we have to iterate over each element in the grid once.
- Space: O(n*m) for the additional matrix we are creating with the same size as our input grid.
'''

from typing import List

def diagonal_travel(grid: List[List[int]]) -> int:
    """
    This function receives a grid and returns the sum of every integer visited during a traversal
    from the top left to the bottom right of the grid.
    Args: n*m integer grid.
    Returns: an integer representing the traversal path sum.
    """
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    matrix = [[0]*m for _ in range(n)]

    matrix[0][0] = grid[0][0]

    for i in range(1, n):
        matrix[i][0] = matrix[i-1][0] + grid[i][0]

    for j in range(1, m):
        matrix[0][j] = matrix[0][j-1] + grid[0][j]

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = max(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + grid[i][j]

    return matrix[-1][-1]