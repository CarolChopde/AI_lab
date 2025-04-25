# AO* Algorithm Implementation
'''
function ao_star(node):
  if node is terminal:
    return True, heuristic

  for each possible child set:
    Recursively evaluate children
    Calculate total cost = edge + heuristic
    Pick child set with min cost

  Update heuristic[node]
  Return status, cost
'''

def ao_star(node):
    """
    Recursive AO* Algorithm
    node: current node to evaluate
    Returns: (status, cost)
    """
    print(f"Expanding node: {node}")

    # node has no children
    if node not in graph or not graph[node]: #node not exists or terminal
        return True, heuristic[node] #alr solved

    solved = False
    min_cost = float('inf')
    best_option = None

    for children, costs in graph[node]:  
        total_cost = 0
        all_solved = True #to make sure all children are solved
        sub_graph = {}

        for i, child in enumerate(children):
            child_solved, child_cost = ao_star(child)
            total_cost += costs[i] + child_cost
            if not child_solved:
                all_solved = False
            sub_graph[child] = child_cost

        if total_cost < min_cost:
            min_cost = total_cost
            best_option = (children, sub_graph)
            solved = all_solved

    heuristic[node] = min_cost
    solution_graph[node] = best_option

    return solved, min_cost

graph = {
    'G': [ 
        (['A'], [4]),               # OR option
        (['B', 'C'], [3, 2])        # AND option
    ],
    'A': [
        (['D', 'E'], [4, 3]),       # AND option
        (['F', 'G1'], [3, 2])       # AND option
    ],
    'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G1': []
}

heuristic = {
    'G': float('inf'), # unknown initially
    'A': 40,
    'B': 21,
    'C': 25,
    'D': 22,
    'E': 26,
    'F': 23,
    'G1': 17
}

solution_graph = {}

# AO* starting from 'G'
solved, cost = ao_star('G')

print("\nSolution Found:", solved)
print("Total Cost from G:", cost)
print("Solution Graph:")
for node in solution_graph:
    print(f"{node} -> {solution_graph[node][0]} (Costs: {solution_graph[node][1]})")
