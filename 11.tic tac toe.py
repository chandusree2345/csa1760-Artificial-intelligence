board = [
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
    [' ', 'X ', 'O']
]
def evaluate(board):
    win_positions = [
        [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], # Rows
        [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], # Columns
        [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]                         # Diagonals
    ]
    for positions in win_positions:
        values = [board[x][y] for x, y in positions]
        if values == ['O'] * 3: return 1
        if values == ['X'] * 3: return -1
    return 0
def minimax(board, is_max):
    score = evaluate(board)
    if score != 0 or not any(' ' in row for row in board):
        return score
    best = -float('inf') if is_max else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O' if is_max else 'X'
                value = minimax(board, not is_max)
                board[i][j] = ' '
                best = max(best, value) if is_max else min(best, value)
    return best
best_move = None
best_val = -float('inf')
for i in range(3):
    for j in range(3):
        if board[i][j] == ' ':
            board[i][j] = 'O'
            move_val = minimax(board, False)
            board[i][j] = ' '
            if move_val > best_val:
                best_val, best_move = move_val, (i, j)
print("Best Move for O:", best_move)
print("Utility Value for the Move:", best_val)
