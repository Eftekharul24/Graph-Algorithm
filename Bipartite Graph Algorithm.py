from collections import deque

def is_bipartite(graph):
    n = len(graph)
    colors = [-1] * n  # Initialize all vertices with no color

    for start in range(n):
        if colors[start] == -1:
            queue = deque()
            queue.append(start)
            colors[start] = 0

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return False
    return True

from collections import deque

def find_bipartition(graph):
    n = len(graph)
    colors = [-1] * n
    partition_A = set()
    partition_B = set()

    for start in range(n):
        if colors[start] == -1:
            queue = deque()
            queue.append(start)
            colors[start] = 0
            partition_A.add(start)

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                        if colors[v] == 0:
                            partition_A.add(v)
                        else:
                            partition_B.add(v)
    return partition_A, partition_B
# Define a graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}

if is_bipartite(graph):
    partition_A, partition_B = find_bipartition(graph)
    print("Partition A:", partition_A)
    print("Partition B:", partition_B)
else:
    print("The graph is not bipartite.")
