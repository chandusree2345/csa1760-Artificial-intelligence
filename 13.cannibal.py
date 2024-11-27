def is_valid(m_left, c_left, m_right, c_right):
    return not ((m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right))
def solve(m_left, c_left, boat_on_left, visited, path):
    if m_left == 0 and c_left == 0:
        print("Solution found!")
        for move in path:
            print(f"Move {move[0]} missionaries and {move[1]} cannibals.")
        return True
    state = (m_left, c_left, boat_on_left)
    if state in visited: return False
    visited.add(state)
    boat_moves = [(2, 0), (1, 1), (0, 2)]
    for m_move, c_move in boat_moves:
        new_m_left, new_c_left = (m_left - m_move, c_left - c_move) if boat_on_left else (m_left + m_move, c_left + c_move)
        new_m_right, new_c_right = 3 - new_m_left, 3 - new_c_left
        new_boat_on_left = not boat_on_left
        if new_m_left >= 0 and new_c_left >= 0 and new_m_right >= 0 and new_c_right >= 0 and is_valid(new_m_left, new_c_left, new_m_right, new_c_right):
            print(f"Trying move: {m_move} missionaries and {c_move} cannibals.")
            print(f"New state: Left Bank: {new_m_left} missionaries, {new_c_left} cannibals. "
                  f"Right Bank: {new_m_right} missionaries, {new_c_right} cannibals.")
            if solve(new_m_left, new_c_left, new_boat_on_left, visited, path + [(m_move, c_move)]):
                return True
    return False
visited, path = set(), []
if not solve(3, 3, True, visited, path):
    print("No solution found.")
