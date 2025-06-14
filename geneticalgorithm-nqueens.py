import random
import time

def generate_individual(N):
    return [random.randint(0, N - 1) for _ in range(N)]  # one queen per row, any col

def fitness(board):
    N = len(board)
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def crossover(p1, p2):
    N = len(p1)
    crossover_point = random.randint(0, N - 1)
    return p1[:crossover_point] + p2[crossover_point:]

def mutate(board, mutation_rate):
    N = len(board)
    new_board = board[:]
    for i in range(N):
        if random.random() < mutation_rate:
            new_board[i] = random.randint(0, N - 1)
    return new_board

def genetic_algorithm(N, pop_size=100, generations=3000, mutation_rate=0.05, elite_size=20):
    start = time.time()
    population = [generate_individual(N) for _ in range(pop_size)]
    for gen in range(generations):
        population = sorted(population, key=fitness)
        best = population[0]
        if fitness(best) == 0:
            return {
                'success': True,
                'solution': best,
                'generation': gen,
                'time_taken': round(time.time() - start, 4)
            }

        new_population = population[:elite_size]  # Elitism
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

    best = min(population, key=fitness)
    return {
        'success': fitness(best) == 0,
        'solution': best,
        'conflicts': fitness(best),
        'time_taken': round(time.time() - start, 4)
    }

if __name__ == "__main__":
    for N in [100]:
        print(f"N = {N}")
        result = genetic_algorithm(N)
        print(result)
        print()
