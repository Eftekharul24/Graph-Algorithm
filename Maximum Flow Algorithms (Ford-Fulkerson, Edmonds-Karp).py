from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Residual capacity

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v, capacity in self.graph[u].items():
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        return visited[t]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Example usage:
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 10)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 4)
    g.add_edge(1, 4, 8)
    g.add_edge(2, 4, 9)
    g.add_edge(3, 5, 10)
    g.add_edge(4, 3, 6)
    g.add_edge(4, 5, 10)

    source = 0
    sink = 5

    max_flow = g.edmonds_karp(source, sink)
    print("Maximum Flow:", max_flow)
