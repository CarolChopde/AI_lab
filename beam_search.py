'''
1. Initialize beam with root
2. Repeat for each depth level:
   a. Expand all nodes in beam
   b. Keep top-k scoring successors
   c. If goal found, stop
'''


import heapq
#User input
def get_distance_matrix(cities):
    distance_matrix = {city: {} for city in cities}
    print("\nEnter distances between cities (only once per pair):")

    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = float(input(f"Distance from {cities[i]} to {cities[j]}: "))
            distance_matrix[cities[i]][cities[j]] = dist
            distance_matrix[cities[j]][cities[i]] = dist

    for city in cities:
        distance_matrix[city][city] = 0  # self-distance = 0

    return distance_matrix

def path_cost(path, matrix):
    cost = 0
    for i in range(1, len(path)):
        cost += matrix[path[i - 1]][path[i]]
    return cost

def calc_distance(route, distance_matrix):
    total_distance = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_distance += distance_matrix[route[-1]][route[0]]  # closing the loop
    return total_distance

#Beam search implementation
def beam_search_tsp(cities, distance_matrix, k):
    n = len(cities)
    beam = [[cities[0]]]  # Start from first city
    iteration = 1

    while True:
        print("\nIteration", iteration)
        heap = []

        for path in beam:
            visited = set(path)
            last = path[-1]

            if len(path) == n:
                full_path = path + [cities[0]]  # Complete the loop
                total_cost = calc_distance(full_path, distance_matrix)
                heapq.heappush(heap, (total_cost, full_path))
                continue

            for city in cities:
                if city not in visited:
                    new_path = path + [city]
                    cost = calc_distance(new_path, distance_matrix)
                    heapq.heappush(heap, (cost, new_path))

        print("Candidates:")
        for cost, path in sorted(heap):
            print("Path:", " → ".join(path), "| Cost:", cost)

        if all(len(p[1]) == n + 1 for p in heap):  # all are complete tours
            break

        beam = []
        for _ in range(min(k, len(heap))):
            cost, path = heapq.heappop(heap)
            beam.append(path)

        print("\nTop", k, "Paths Selected:")
        for p in beam:
            print(" → ".join(p))

        iteration += 1

    best = min(heap)
    print("\nFinal Best Path:", " → ".join(best[1]))
    print("Total Distance:", best[0])
    return best

num_cities = int(input("Enter number of cities: "))
cities = [input(f"Enter city {i + 1} name: ") for i in range(num_cities)]
distance_matrix = get_distance_matrix(cities)

beam_width = int(input("\nEnter Beam Width (k): "))
beam_search_tsp(cities, distance_matrix, beam_width)












    
