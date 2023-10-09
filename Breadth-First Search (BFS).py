from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs(self, start_vertex):
        visited = [False] * len(self.graph)
        queue = deque()

        visited[start_vertex] = True
        queue.append(start_vertex)

        print("Breadth-First Traversal starting from vertex", start_vertex)

        while queue:
            current_vertex = queue.popleft()
            print("Visited vertex:", current_vertex)

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

# Create a graph and add edges
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

# Perform BFS starting from vertex 0
graph.bfs(0)
