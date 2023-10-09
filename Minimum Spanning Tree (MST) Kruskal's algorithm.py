class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(graph):
    edges = [(weight, u, v) for u, v, weight in graph]
    edges.sort()

    n = len(edges)
    mst = []
    uf = UnionFind(n)

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            mst.append((u, v, weight))
            uf.union(u, v)

    return mst

# Example usage:
if __name__ == "__main__":
    # Define a sample graph as a list of (u, v, weight) tuples
    graph = [
        (0, 1, 2),
        (0, 2, 4),
        (1, 2, 1),
        (1, 3, 7),
        (2, 3, 3),
    ]

    minimum_spanning_tree = kruskal(graph)
    print("Minimum Spanning Tree:")
    for u, v, weight in minimum_spanning_tree:
        print(f"Edge: {u} - {v}, Weight: {weight}")
