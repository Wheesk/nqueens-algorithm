import random
import math
import time

def calculate_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_smart_neighbor(board):
    n = len(board)
    new_board = board[:]
    row = random.randint(0, n - 1)
    min_conflicts = float('inf')
    best_col = new_board[row]

    for col in range(n):
        if col == board[row]:
            continue
        new_board[row] = col
        conflicts = calculate_conflicts(new_board)
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            best_col = col
    new_board[row] = best_col
    return new_board

def simulated_annealing(N, max_steps=500000):
    import random, time, math

    def conflicts(board):
        c = 0
        for i in range(N):
            for j in range(i + 1, N):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    c += 1
        return c

    def random_neighbor(board):
        row = random.randint(0, N - 1)
        new_col = random.randint(0, N - 1)
        while new_col == board[row]:
            new_col = random.randint(0, N - 1)
        new = board[:]
        new[row] = new_col
        return new

    board = [random.randint(0, N - 1) for _ in range(N)]
    current = board[:]
    current_conflicts = conflicts(current)
    best = current[:]
    best_conflicts = current_conflicts

    T = N  # scale temperature with N
    start = time.time()

    for step in range(max_steps):
        if current_conflicts == 0:
            break

        neighbor = random_neighbor(current)
        neighbor_conflicts = conflicts(neighbor)
        delta = neighbor_conflicts - current_conflicts

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbor
            current_conflicts = neighbor_conflicts
            if current_conflicts < best_conflicts:
                best = current
                best_conflicts = current_conflicts

        T = T * 0.999  # slow cooling

        if T < 0.001:
            T = N  # reheating

    end = time.time()
    return {
        'success': best_conflicts == 0,
        'solution': best if best_conflicts == 0 else None,
        'conflicts': best_conflicts,
        'time_taken': round(end - start, 2)
    }


if __name__ == "__main__":
    for N in [100]:
        print(f"Simulated Annealing: N = {N}")
        result = simulated_annealing(N)
        print(result)
        print()
