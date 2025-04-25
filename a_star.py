'''
1. Initialize open_list with start node (f = h)
2. While open_list not empty:
   a. Remove node with lowest f
   b. If goal, reconstruct path
   c. For each neighbor:
      - If new path is better:
        - Update cost and parent
        - Add to open_list
'''



#a_star
import heapq #priority queue - h(n)

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic #estimate of the cost from this node to the goal
        self.neighbors = []  # List of (neighbor_node, cost)

def a_star_search(start_node, goal_name):
    open_list = [] # 3 tuple storing f(n), g(n), node
    heapq.heappush(open_list, (start_node.heuristic, 0, start_node)) #g(n) = 0 for start node
    parent_map = {}
    g_cost = {}
    g_cost[start_node.name] = 0
    visited = set()

    while open_list:
        f, current_g, current_node = heapq.heappop(open_list)

        if current_node.name == goal_name:
            path = []
            total_distance = g_cost[goal_name]
            node = goal_name
            while node in parent_map:
                path.append(node)
                node = parent_map[node]
            path.append(start_node.name)
            path.reverse()
            return path, total_distance

        visited.add(current_node.name)

        for neighbor, cost in current_node.neighbors:
            if neighbor.name in visited: #alr explored so skip it 
                continue

            tentative_g = g_cost[current_node.name] + cost
            if neighbor.name not in g_cost or tentative_g < g_cost[neighbor.name]:
                g_cost[neighbor.name] = tentative_g
                f_cost = tentative_g + neighbor.heuristic
                heapq.heappush(open_list, (f_cost, tentative_g, neighbor))
                parent_map[neighbor.name] = current_node

    return [], 0  # No path found

# Example Graph
A = Node("A", 6)
B = Node("B", 4)
C = Node("C", 2)
D = Node("D", 0)

A.neighbors = [(B, 1), (C, 4)]
B.neighbors = [(C, 2), (D, 5)]
C.neighbors = [(D, 1)]

# Run A* Search from A to D
path, distance = a_star_search(A, "D")

if path:
    print("Path found:", " -> ".join(path))
    print("Total distance:", distance)
else:
    print("No path found.")

