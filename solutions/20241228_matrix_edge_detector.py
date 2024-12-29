'''
Problem Description:
Given a 2D integer matrix, where each value represents a pixel color. We are required to write a function that outputs a binary 2D matrix as an edge map of the given matrix. An edge in the image is defined as a boundary between two different pixel colors.

Solution Approach:
Our approach will be to traverse the matrix using nested loop (for each pixel), and then, for each pixel we will inspect the surrounding pixels (top, down, left, right). If we find any pixel of different color, we will mark that pixel as edge in the result binary matrix. To handle the wrapping around, we will take a mod with n (row size) or m (column size) while checking for neighbors.

Complexity Analysis:
- Time: O(n*m) where n is the row size and m is the column size since we are checking each pixel and their immediate neighbors.
- Space: O(n*m) where n and m are the dimensions of the matrix because we are storing the binary matrix output.

'''

def detect_edges(matrix):
    """
    Given a 2D integer matrix, produces a binary matrix to depict edge in the image.
    Args: matrix: List[List[int]], a 2D list where each integer represents a pixel color
    Returns: List[List[int]],   A binary 2D matrix where 1 marks an edge and 0 marks absence of edge.
    """
    n, m = len(matrix), len(matrix[0])
    res = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != matrix[(i+1)%n][j] or matrix[i][j] != matrix[i][(j+1)%m]: 
                res[i][j] = 1
    return res
