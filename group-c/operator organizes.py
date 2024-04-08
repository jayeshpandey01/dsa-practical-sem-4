# Tour operator organizes guided bus trips across the Maharashtra. Tourists may have 
# different preferences. Tour operator offers a choice from many different routes. Every 
# day the bus moves from starting city S to another city F as chosen by client. On this way, 
# the tourists can see the sights alongside the route travelled from S to F. Client may have 
# preference to choose route. There is a restriction on the routes that the tourists may 
# choose from, the bus has to take a short route from S to F or a route having one distance 
# unit longer than the minimal distance. Two routes from S to F are considered different if 
# there is at least one road from a city A to a city B which is part of one route, but not of 
# the other route.  

import heapq

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_edge(self, source, destination, distance):
        self.vertices.add(source)
        self.vertices.add(destination)
        if source not in self.edges:
            self.edges[source] = []
        if destination not in self.edges:
            self.edges[destination] = []
        self.edges[source].append((destination, distance))
        self.edges[destination].append((source, distance))

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, edge_distance in graph.edges[current_vertex]:
            distance = current_distance + edge_distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage:
graph = Graph()
graph.add_edge("Mumbai", "Pune", 200)
graph.add_edge("Mumbai", "Nashik", 180)
graph.add_edge("Pune", "Nashik", 160)
graph.add_edge("Pune", "Kolhapur", 250)
graph.add_edge("Nashik", "Kolhapur", 300)

# Client preferences
start_city = "Mumbai"
destination_city = "Kolhapur"
preferred_distance = 220

# Compute shortest paths from start city to all other cities
shortest_paths = dijkstra(graph, start_city)

# Filter routes based on preferences
possible_routes = [(destination, distance) for destination, distance in shortest_paths.items() if distance <= preferred_distance + 1]

print("Possible routes:")
for destination, distance in possible_routes:
    print(f"Route from {start_city} to {destination}: Distance = {distance}")

