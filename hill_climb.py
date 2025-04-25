'''
1. Start with initial state
2. Loop:
   a. Evaluate all neighbors
   b. Move to the one with best score
   c. If no improvement, stop
'''


import random

def calculate_conflicts(board):
    # calculate number of queen conflicts (attacks)
    # conflicts occur when queens share columns or diagonals
    # assume no row conflicts since each queen is in a different row
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            # check column conflict
            if board[i] == board[j]:
                conflicts += 1
            # check diagonal conflict
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_random_neighbor(board):
    # generate a random neighbor by swapping two positions
    # this is the stochastic part: random move instead of exhaustive search
    neighbor = board.copy()
    n = len(neighbor)
    i, j = random.sample(range(n), 2)  # pick two random indices
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def stochastic_hill_climbing(n, max_steps=100):
    print(f"Running stochastic hill climbing for N = {n} queens, max steps = {max_steps}")
    # initial random population of solutions
    # each individual is represented as (a, b, c, d) for N=4, etc.
    current = list(range(n))
    random.shuffle(current)  # randomize initial state
    
    # track steps to avoid infinite loops
    for step in range(max_steps):
        current_conflicts = calculate_conflicts(current)
        
        # goal check: zero conflicts means solution found
        if current_conflicts == 0:
            return current, step
        
        # get a random neighbor (stochastic move)
        neighbor = get_random_neighbor(current)
        neighbor_conflicts = calculate_conflicts(neighbor)
        
        # accept neighbor if it’s better (fewer conflicts)
        if neighbor_conflicts <= current_conflicts:
            current = neighbor
    
    print(f"Reached max steps ({max_steps}), stopping.")
    print("Final state:")
    print_board(current)
    print(f"Conflicts: {calculate_conflicts(current)}")
    # return None if no solution found within max_steps
    return None, max_steps

def print_board(board):
    # shows queen positions with 'Q' and empty spots with '.'
    n = len(board)
    for row in range(n):
        line = ['.' for _ in range(n)]
        line[board[row]] = 'Q'
        print(' '.join(line))

if __name__ == "__main__":
    n = 8  
    solution, steps = stochastic_hill_climbing(n)
    
    if solution:
        print(f"Solution found in {steps} steps:")
        print_board(solution)
        print(f"Conflicts: {calculate_conflicts(solution)}")
    else:
        print("No solution found within max steps.")
