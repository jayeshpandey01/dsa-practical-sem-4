# Represent a given graph using adjacency matrix/list to perform DFS and using adjacency 
# list to perform BFS. Use the map of the area around the college as the graph. Identify the 
# prominent land marks as nodes and perform DFS and BFS on that. 

from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)

# Define landmarks as nodes
landmarks = ["Building A", "Building B", "Park", "Street 1", "Street 2", "Cafeteria"]
# Define connections between landmarks
connections = [
    ("Building A", "Building B"),
    ("Building A", "Park"),
    ("Building B", "Park"),
    ("Park", "Street 1"),
    ("Park", "Street 2"),
    ("Building A", "Cafeteria"),
    ("Building B", "Cafeteria")
]


def dfs(graph, start_node):
    visited = set()

    def dfs_helper(node):
        visited.add(node)
        print(node)

        for neighbor in graph.adjacency_list[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start_node)

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph.adjacency_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
graph = Graph()

# Add landmarks as nodes
for landmark in landmarks:
    graph.add_node(landmark)

# Add connections between landmarks
for connection in connections:
    graph.add_edge(connection[0], connection[1])

# Perform DFS starting from "Building A"
print("DFS:")
dfs(graph, "Building A")

# Perform BFS starting from "Building A"
print("\nBFS:")
bfs(graph, "Building A")

