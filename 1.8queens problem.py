def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col):
    # Base case: If all queens are placed
    if col >= len(board):
        print_board(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            res = solve_queens(board, col + 1) or res
            board[i][col] = 0  # Backtrack

    return res

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_queens(board, 0):
        print("No solution exists")
    else:
        print("Solutions printed above")

# Test the function with 8 queens
solve_n_queens(8)
