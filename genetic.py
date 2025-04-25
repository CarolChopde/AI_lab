'''
1. Generate initial population
2. Repeat:
   a. Evaluate fitness
   b. Select parents
   c. Crossover to produce offspring
   d. Apply mutation
   e. Replace population with new generation
3. Stop when solution found or max generations reached
'''


import random

# target equation function
def equation(a, b, c, d):
    return a + 2 * b + 3 * c + 4 * d

# initial random population of solutions
def generate_population(size):
    population = []

    for _ in range(size):
        # each individual is represented as (a, b, c, d)
        individual = (random.randint(0, 30), random.randint(0, 15), random.randint(0, 10), random.randint(0, 7))
        population.append(individual)
    return population

# fitness function
def fitness(individual):
    # compute the absolute difference from target value
    return abs(30 - equation(*individual))

# select parents for crossover based on fitness
def select_parents(population):
    sorted_population = sorted(population, key=fitness)  
    return sorted_population[:2]  # select top 2 fittest individuals

# perform crossover between two parents
def crossover(parent1, parent2):
    # single-point crossover
    point = random.randint(1, 3)  # choose a crossover point

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    print(f"Crossover point: {point}, Children: {child1}, {child2}")
    return child1, child2

# apply mutation to an individual
def mutate(individual, mutation_rate):
    individual = list(individual)  
    for i in range(len(individual)): 
        if random.random() < mutation_rate:  # apply mutation with given probability
            individual[i] = random.randint(0, 30)
    mutated_individual = tuple(individual) 
    print(f"Mutation applied: {mutated_individual}")
    return mutated_individual

def genetic_algorithm(population_size=10, generations=100, mutation_rate=0.1):
    population = generate_population(population_size)  # initialize population
    print("Initial Population:")
    for individual in population:
        print(f"Chromosome: {individual}, Fitness: {fitness(individual)}")
    
    for generation in range(generations):
        print(f"\nGeneration {generation}")
        
        # check if any solution satisfies the equation
        for individual in population:
            if equation(*individual) == 30:
                print(f"Solution found in generation {generation}: {individual}")
                print("Genetic algorithm successfully found a solution.")
                return individual
        
        # select parents from population
        parent1, parent2 = select_parents(population)
        print(f"Selected Parents: {parent1}, {parent2}")
        
        # generate offspring through crossover
        child1, child2 = crossover(parent1, parent2)
        
        # apply mutation
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        
        # create new population keeping top individuals
        population = select_parents(population) + [child1, child2]
        population += generate_population(population_size - len(population))  # fill the rest of the population
    
    best_solution = min(population, key=fitness)
    print(f"Best solution found: {best_solution}, fitness: {fitness(best_solution)}")
    print("Genetic algorithm was unable to find an exact solution.")

    return best_solution

if __name__ == "__main__":
    genetic_algorithm(population_size=10, generations=100, mutation_rate=0.1)
