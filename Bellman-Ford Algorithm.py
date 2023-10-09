class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Initialize distances from the source vertex to all other vertices as infinity
        distances = [float('inf')] * self.V
        distances[src] = 0

        # Relax all edges (V-1) times to find the shortest paths
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the shortest distances from the source vertex
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(i, "\t", distances[i])

# Example usage
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 8)
g.add_edge(1, 2, -3)
g.add_edge(1, 3, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 4, 2)
g.add_edge(4, 1, -1)

source = 0
g.bellman_ford(source)
