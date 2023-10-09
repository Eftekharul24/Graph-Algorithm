import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        min_cost = 0
        visited = [False] * self.V
        min_heap = []

        # Start with the first vertex
        heapq.heappush(min_heap, (0, 0))  # (weight, vertex)

        while min_heap:
            # Get the vertex with the minimum weight
            weight, u = heapq.heappop(min_heap)

            # If the vertex has already been visited, skip it
            if visited[u]:
                continue

            # Include the vertex in the minimum spanning tree
            visited[u] = True
            min_cost += weight

            # Add adjacent vertices to the priority queue
            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))

        return min_cost

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    min_cost = g.prim_mst()
    print("Minimum Spanning Tree Cost:", min_cost)
