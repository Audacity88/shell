from math import floor, ceil
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.edges = []
        self.vertices = []
        self.adj_matrix = np.zeros((num_vertices, num_vertices))
        self.generate_graph()

    def generate_graph(self):
        """Generate a random graph with the specified number of vertices and edges"""
        self.vertices = list(range(self.num_vertices))
        while len(self.edges) < self.num_edges:
            u, v = random.sample(self.vertices, 2)
            if (u, v) not in self.edges and (v, u) not in self.edges:
                self.edges.append((u, v))
                self.adj_matrix[u][v] = 1
                self.adj_matrix[v][u] = 1

    def stcon(self, s, t):
        """Test whether a path exists from s to t"""
        return self.k_edge_path(s, t, self.num_vertices)

    def k_edge_path(self, s, t, k):
        """Test whether a path of length at most k exists from s to t"""
        if k == 0:
            return s == t
        if k == 1:
            return self.adj_matrix[s][t] == 1
        for u in self.vertices:
            if self.adj_matrix[s][u] == 1 and self.k_edge_path(u, t, k-1):
                return True
        return False

    def dijkstra(self, s, t):
        """Find the shortest path between s and t using Dijkstra's algorithm"""
        dist = [float('inf')] * self.num_vertices
        dist[s] = 0
        visited = set()
        while len(visited) < self.num_vertices:
            u = min(set(range(self.num_vertices)) - visited, key=lambda v: dist[v])
            visited.add(u)
            for v in self.vertices:
                if self.adj_matrix[u][v] == 1:
                    alt = dist[u] + 1
                    if alt < dist[v]:
                        dist[v] = alt
        return dist[t]

# Create a graph with 10 vertices and 5 edges
G = Graph(10, 5)

# Test whether a path exists from vertex 0 to vertex 9
print(G.stcon(0, 9))

# Find the shortest path between vertex 0 and vertex 9
print(G.dijkstra(0, 9))

# Plot the adjacency matrix
plt.imshow(G.adj_matrix, cmap='gray', interpolation='none')
plt.show()

