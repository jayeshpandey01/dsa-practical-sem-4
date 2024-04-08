# There are flight paths between cities. If there is a flight between city A and city B then 
# there is an edge between the cities. The cost of the edge can be the time that flight take 
# to reach city B from A, or the amount of fuel used for the journey. Represent this as a 
# graph. The node can be represented by airport name or name of the city. Use adjacency 
# list representation of the graph or use adjacency matrix representation of the graph. 
# Check whether the graph is connected or not. Justify the storage representation used. 


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}
        self.adjacency_matrix = [[0] * len(vertices) for _ in range(len(vertices))]

    def add_edge(self, source, destination, cost):
        self.adjacency_list[source].append((destination, cost))
        self.adjacency_matrix[self.vertices.index(source)][self.vertices.index(destination)] = cost

def is_connected(graph):
    visited = set()
    stack = [list(graph.vertices)[0]]  # Start DFS from the first vertex

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, _ in graph.adjacency_list[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return len(visited) == len(graph.vertices)

# Example usage:
vertices = ["City A", "City B", "City C", "City D"]

# Create a graph using adjacency list representation
graph_adj_list = Graph(vertices)
graph_adj_list.add_edge("City A", "City B", 10)
graph_adj_list.add_edge("City B", "City C", 20)
graph_adj_list.add_edge("City C", "City D", 30)
graph_adj_list.add_edge("City D", "City A", 40)

# Create a graph using adjacency matrix representation
graph_adj_matrix = Graph(vertices)
graph_adj_matrix.add_edge("City A", "City B", 10)
graph_adj_matrix.add_edge("City B", "City C", 20)
graph_adj_matrix.add_edge("City C", "City D", 30)
graph_adj_matrix.add_edge("City D", "City A", 40)

# Check if the graphs are connected
print("Graph connected (Adjacency List):", is_connected(graph_adj_list))
print("Graph connected (Adjacency Matrix):", is_connected(graph_adj_matrix))

