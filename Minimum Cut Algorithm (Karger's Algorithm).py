import random

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def contract(self):
        n = len(self.vertices)
        while n > 2:
            # Randomly select an edge
            random_edge = random.choice(self.edges)
            u, v = random_edge

            # Merge vertices u and v into a single vertex
            self.vertices[u] = self.vertices.get(u, []) + self.vertices.get(v, [])
            del self.vertices[v]

            # Update edges to remove self-loops
            self.edges = [(x, y) for x, y in self.edges if x != v and y != v]

            # Update edges to replace v with u
            self.edges = [(u, y) if x == v else (x, y) for x, y in self.edges]

            n -= 1

    def min_cut(self):
        while len(self.vertices) > 2:
            self.contract()
        # The remaining edges represent the minimum cut
        return len(self.edges)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 4)

    num_trials = 1000  # Number of trials to increase accuracy
    min_cut = float('inf')

    for _ in range(num_trials):
        current_cut = g.min_cut()
        if current_cut < min_cut:
            min_cut = current_cut

    print("Minimum Cut:", min_cut)
