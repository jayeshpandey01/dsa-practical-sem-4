# You have a business with several offices; you want to lease phone lines to connect them 
# up with each other; and the phone company charges different amounts of money to 
# connect different pairs of cities. You want a set of lines that connects all your offices with 
# a minimum total cost. Solve the problem by suggesting appropriate data structures.  

import heapq

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.vertices.add(source)
        self.vertices.add(destination)
        self.edges.append((weight, source, destination))

def prim(graph):
    # Initialize an empty MST and a set to track visited vertices
    mst = []
    visited = set()

    # Choose a random vertex as the starting point
    start_vertex = next(iter(graph.vertices))
    visited.add(start_vertex)

    # Initialize a priority queue with edges from the starting vertex
    pq = [(weight, source, destination) for weight, source, destination in graph.edges if source == start_vertex]
    heapq.heapify(pq)

    # Repeat until all vertices are visited
    while pq and len(visited) < len(graph.vertices):
        weight, source, destination = heapq.heappop(pq)
        if destination not in visited:
            visited.add(destination)
            mst.append((weight, source, destination))
            for edge_weight, next_source, next_destination in graph.edges:
                if next_source == destination and next_destination not in visited:
                    heapq.heappush(pq, (edge_weight, next_source, next_destination))
                elif next_destination == destination and next_source not in visited:
                    heapq.heappush(pq, (edge_weight, next_destination, next_source))

    return mst

# Example usage:
graph = Graph()
graph.add_edge("Office 1", "Office 2", 5)
graph.add_edge("Office 1", "Office 3", 10)
graph.add_edge("Office 2", "Office 3", 8)
graph.add_edge("Office 2", "Office 4", 7)
graph.add_edge("Office 3", "Office 4", 3)

mst = prim(graph)
print("Minimum Spanning Tree (MST):", mst)

