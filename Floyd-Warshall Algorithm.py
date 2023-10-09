INF = float("inf")

def floyd_warshall(graph):
    num_vertices = len(graph)
    
    # Initialize the distance matrix with the graph
    dist = [[0 if i == j else graph[i][j] if j in graph[i] else INF for j in range(num_vertices)] for i in range(num_vertices)]
    
    # Update the distance matrix by considering all possible paths
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example usage:
graph = {
    0: {1: 2, 2: 4},
    1: {2: 1, 3: 7},
    2: {3: 3},
    3: {0: 5}
}

# Find the shortest paths between all pairs of vertices
result = floyd_warshall(graph)

# Print the shortest distance matrix
for row in result:
    print(row)
