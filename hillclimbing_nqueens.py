import random
import time

def calculate_conflicts(board):
    n = len(board)
    row_conflict = [0] * n
    diag1 = [0] * (2 * n)
    diag2 = [0] * (2 * n)
    for row, col in enumerate(board):
        row_conflict[row] += 1
        diag1[row + col] += 1
        diag2[row - col + n] += 1
    conflicts = 0
    for row, col in enumerate(board):
        conflicts += (diag1[row + col] - 1)
        conflicts += (diag2[row - col + n] - 1)
    return conflicts // 2

def get_best_move(board):
    n = len(board)
    min_conflicts = calculate_conflicts(board)
    best_move = board[:]
    for row in range(n):
        original = board[row]
        for col in range(n):
            if col == original:
                continue
            board[row] = col
            conflicts = calculate_conflicts(board)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_move = board[:]
        board[row] = original
    return best_move, min_conflicts

def hill_climbing(N, max_restarts=30, max_steps=500):
    start_time = time.time()
    for restart in range(max_restarts):
        board = [random.randint(0, N - 1) for _ in range(N)]
        for step in range(max_steps):
            current_conflicts = calculate_conflicts(board)
            if current_conflicts == 0:
                return {
                    'success': True,
                    'solution': board,
                    'steps': step,
                    'restarts': restart,
                    'time_taken': round(time.time() - start_time, 4)
                }
            next_board, next_conflicts = get_best_move(board)
            if next_conflicts >= current_conflicts:
                break  # Local minimum → restart
            board = next_board
    return {
        'success': False,
        'solution': None,
        'time_taken': round(time.time() - start_time, 4)
    }

if __name__ == "__main__":
    for N in [120]:
        print(f"N = {N}")
        result = hill_climbing(N)
        print(result)
        print()
