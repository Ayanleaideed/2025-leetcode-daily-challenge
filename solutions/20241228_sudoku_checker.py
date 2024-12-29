'''
Problem Description:
The problem requires us to verify if it is safe to put a digit in a given cell of a Sudoku game. It is safe if the digit does not occur in the same row, column, or 3x3 sub-grid on the current board.

Solution Approach:
The core algorithm is to iteratively check the row, the column, and the sub-grid (box) if the digit under consideration is present. 
- First, check every cell in the row to see if the digit is already there.
- Second, check every cell in the column to see if the digit is already there.
- Finally, check every cell in the sub-grid (box) to see if the digit is already there.
- If the digit is already present in the row, column, or sub-grid, return False. Otherwise, return True.

Complexity Analysis:
- Time: O(1), as the function is always checking a fixed size board and a specific cell number.
- Space: O(1), as we do not use any extra space that grows with inputs.

'''

def isSafe(board, row, col, num):
    """
    A function to check if it is safe to put a given digit in a certain cell on the Sudoku board.
    Args: 
    - board: a 9x9 2D list of integers, representing the Sudoku board.
    - row, col: integers, representing the row and column indices of the cell.
    - num: integer, the digit to be placed in the cell.
    Returns: 
    A boolean, True if it is safe to put the num in the given cell; False otherwise.
    """

    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    for x in range(9):
        # Checking in row
        if board[row][x] == num:
            return False
             
        # Checking in column
        if board[x][col] == num:
            return False
 
        # Checking in3x3 box
        if board[3 * (row // 3) + x // 3][3 * (col // 3) + x % 3] == num:
            return False
 
    return True
