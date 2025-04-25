'''
1. Add start node to open_list
2. While open_list not empty:
   a. Pop node with smallest h
   b. If goal, return path
   c. For each neighbor:
      - If not visited:
        - Add to open_list
'''


import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic  # h(n)
        self.neighbors = []        # list of (neighbor, cost)

def greedy_best_first_search(start_node, goal_node):
    open_list = []
    heapq.heappush(open_list, (start_node.heuristic, start_node))
    
    visited = set()
    parent_map = {}
    g_cost = {start_node.name: 0}  # g(n): actual distance from start node

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.name == goal_node.name:
            path = []
            total_distance = g_cost[goal_node.name]
            node = goal_node.name
            while node in parent_map:
                path.append(node)
                node = parent_map[node]
            path.append(start_node.name)
            path.reverse()
            return path, total_distance

        visited.add(current_node.name)

        for neighbor, cost in current_node.neighbors:
            if neighbor.name not in visited:
                heapq.heappush(open_list, (neighbor.heuristic, neighbor))
                visited.add(neighbor.name)
                parent_map[neighbor.name] = current_node.name
                g_cost[neighbor.name] = g_cost[current_node.name] + cost

    return [], 0  # No path found

# Example Graph
A = Node("A", 10)
B = Node("B", 8)
C = Node("C", 5)
D = Node("D", 7)
E = Node("E", 0)

A.neighbors = [(B, 1), (C, 4)]
B.neighbors = [(D, 2), (E, 7)]
C.neighbors = [(E, 5)]
D.neighbors = [(E, 1)]
E.neighbors = []

# Run Greedy Best First Search
path, total_distance = greedy_best_first_search(A, E)

print("Path found:", " -> ".join(path))
print("Total distance:", total_distance)
