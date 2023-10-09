from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def dfs(self, vertex, visited):
        visited[vertex] = True
        print("Visited vertex:", vertex)

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def depth_first_search(self, start_vertex):
        visited = [False] * len(self.graph)
        self.dfs(start_vertex, visited)

# Create a graph and add edges
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

print("Depth-First Traversal starting from vertex 0:")
graph.depth_first_search(0)
