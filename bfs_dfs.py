#bfs
from collections import deque

def bfs(initial_state, goal_state, transitions):
    frontier = deque()
    visited = set()
    parent_map = {}

    frontier.append(initial_state) #start with root
    visited.add(initial_state)
    parent_map[initial_state] = None #root has no parent

    while frontier: #not empty
        current_node = frontier.popleft()

        if current_node == goal_state:
            # Reconstruct and print path
            path = []
            node = goal_state
            while node is not None:
                path.append(node)
                node = parent_map[node]
            path.reverse()
            print("Goal found! Path:", ' '.join(map(str, path)))
            return True

        for neighbor in transitions.get(current_node, []):
            if neighbor not in visited:
                frontier.append(neighbor)
                visited.add(neighbor)
                parent_map[neighbor] = current_node

    print("Goal not found.")
    return False

# Example usage
if __name__ == "__main__":
    num_edges = int(input("Enter the number of edges: "))
    transitions = {}

    print("Enter the edges (format: start_vertex end_vertex):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        transitions.setdefault(u, []).append(v)
        transitions.setdefault(v, []).append(u)

    initial_state = int(input("Enter the initial state: "))
    goal_state = int(input("Enter the goal state: "))
    bfs(initial_state, goal_state, transitions)

#dfs-------------------------------------------------
def dfs(initial_state, goal_state, transitions):
    frontier = [initial_state]
    explored = set()
    parent_map = {}
    
    parent_map[initial_state] = None

    while frontier:
        current_node = frontier.pop()

        if current_node == goal_state:
            # Reconstruct and print path
            path = []
            node = goal_state
            while node is not None:
                path.append(node)
                node = parent_map[node]
            path.reverse()
            print("Goal found! Path:", ' '.join(map(str, path)))
            return True

        if current_node not in explored:
            explored.add(current_node)
            for neighbor in transitions.get(current_node, []):
                if neighbor not in explored and neighbor not in frontier:
                    frontier.append(neighbor)
                    parent_map[neighbor] = current_node

    print("Goal not found.")
    return False

# Example usage
if __name__ == "__main__":
    num_edges = int(input("Enter the number of edges: "))
    transitions = {}

    print("Enter the edges (format: start_vertex end_vertex):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        transitions.setdefault(u, []).append(v)
        transitions.setdefault(v, []).append(u)

    initial_state = int(input("Enter the initial state: "))
    goal_state = int(input("Enter the goal state: "))
    dfs(initial_state, goal_state, transitions)
