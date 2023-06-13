def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def is_valid(board, num, row, col):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_start_row + i][box_start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    row, col = find_empty_cell(board)

    # Base case: if no empty cell found, puzzle solved
    if row is None and col is None:
        return True

    # Try numbers from 1 to 9
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            # Recursively solve the puzzle
            if solve_sudoku(board):
                return True

            # If the puzzle is not solved, backtrack
            board[row][col] = 0

    # If no number from 1 to 9 works, the puzzle is unsolvable
    return False

def print_board(board):
    for row in board:
        print(row)

# Example Sudoku puzzle
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

if solve_sudoku(board):
    print("Sudoku puzzle solved:")
    print_board(board)
else:
    print("No solution exists for the Sudoku puzzle.")
