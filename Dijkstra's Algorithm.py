Dijkstra's algorithm can be implemented in Python to find the shortest path from a source vertex to all other vertices in a weighted graph. Below is a Python implementation of Dijkstra's algorithm using an adjacency list representation:

```python
import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # For an undirected graph

    def dijkstra(self, src):
        # Initialize distances and visited list
        distances = [float('inf')] * self.vertices
        distances[src] = 0
        visited = [False] * self.vertices

        # Create a priority queue (min heap) to store vertices and their distances
        priority_queue = [(0, src)]

        while priority_queue:
            dist_u, u = heapq.heappop(priority_queue)

            # If the vertex is already visited, skip
            if visited[u]:
                continue

            visited[u] = True

            # Update the distances to adjacent vertices
            for v, weight in self.graph[u]:
                if not visited[v] and dist_u + weight < distances[v]:
                    distances[v] = dist_u + weight
                    heapq.heappush(priority_queue, (distances[v], v))

        # Print the shortest distances from the source vertex
        print("Vertex \t Distance from Source")
        for i in range(self.vertices):
            print(i, "\t", distances[i])

# Example usage
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 8)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

source = 0
g.dijkstra(source)
```

In this Python implementation, we create a `Graph` class with methods to add edges and perform Dijkstra's algorithm to find the shortest paths. You can modify the edges and weights by calling the `add_edge` method and change the `source` variable to specify the source vertex from which you want to find the shortest paths. The program will print the shortest distances from the source vertex to all other vertices.
