#Author: Ayanle A 
#Date: 01/05/2025



'''
Problem Description:
The problem is to find the largest rectangle filled with 1's and has 0's border in the given binary 2D matrix. If no such rectangle exists, return 0.

Solution Approach:
I will use dynamic programming approach for this problem. I will create a 2D dp list containing lists containing 0 initially. Then, I will iterate over each row in reverse order and each column in normal order. If the element at the particular index of matrix is 1, then if the column is not the last one, I will add dp[row][column + 1] to dp[row][column] and add 1 to dp[row][column], if column is the last one, then I will just add 1 to dp[row][column]. Then, I will iterate over the row and every column from that column to the last column and will find the minimum of that row's all columns value, multiply it with the index difference + 1 and find the maximum of all those and store it in res. At the end, return res as it will contain the size of the largest rectangle surrounded by 0's.

Complexity Analysis:
- Time: O(N^2M) as in the worst case, we might have to iterate over the elements M*N^2 times, where M is the number of rows and N is the number of columns.
- Space: O(MN) for the dp array, where M is the number of rows and N is the number of columns.
'''

def maximalRectangleBorders(matrix):
    """
    Find the largest rectangle filled with 1's and has 0's border.
    Args: matrix: List[List[int]]: a 2D binary matrix.
    Returns: int: the size of the largest rectangle surrounded by 0's.
    """
    if not matrix or not matrix[0]: 
        return 0
       
    dp = [[0]*(len(matrix[0]) + 1) for _ in range(len(matrix))]
 
    res = 0
    for row in range(len(matrix) - 1, -1, -1):
        for col in range(len(matrix[row])):
            # Checking for 1's
            if matrix[row][col] == "1":
                # Building DP matrix
                dp[row][col] = dp[row][col + 1] + 1 if col < len(matrix[row]) - 1 else 1
                current = dp[row][col]
                for line in range(row, len(matrix)):
                    current = min(current, dp[line][col])
                    if current == 0: 
                        break
                    res = max(res, current * (line - row + 1))                   
    return res
