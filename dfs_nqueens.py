import time

def is_safe(position, row, col):
    for r in range(row):
        c = position[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_dfs(N):
    solutions = []
    position = [-1] * N  # position[i] = column of queen in row i

    def backtrack(row):
        if row == N:
            solutions.append(position.copy())
            return
        for col in range(N):
            if is_safe(position, row, col):
                position[row] = col
                backtrack(row + 1)
                position[row] = -1  # backtrack

    start = time.time()
    backtrack(0)
    end = time.time()

    return {
        'solutions_found': len(solutions),
        'first_solution': solutions[0] if solutions else None,
        'time_taken': round(end - start, 4),
    }

if __name__ == "__main__":
    for N in [13]:
        print(f"Running DFS for N = {N}")
        result = solve_dfs(N)
        print(f"Solutions Found: {result['solutions_found']}")
        print(f"First Solution: {result['first_solution']}")
        print(f"Time Taken: {result['time_taken']} seconds\n")
