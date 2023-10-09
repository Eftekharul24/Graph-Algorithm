from collections import defaultdict, deque

def spfa(graph, start):
    # Initialize distance dictionary with infinity for all nodes except the start node
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    # Create a queue for the SPFA algorithm
    queue = deque([start])

    # Create a dictionary to keep track of the number of times each node is enqueued
    enqueued_count = defaultdict(int)
    enqueued_count[start] = 1

    while queue:
        node = queue.popleft()

        # Relax edges from the current node
        for neighbor, weight in graph[node]:
            if distance[node] + weight < distance[neighbor]:
                distance[neighbor] = distance[node] + weight

                # Enqueue the neighbor if it is not already in the queue
                if enqueued_count[neighbor] == 0:
                    queue.append(neighbor)
                    enqueued_count[neighbor] += 1

                    # Check for negative-weight cycles (optional)
                    if enqueued_count[neighbor] >= len(graph):
                        return "Negative-weight cycle detected"

    return distance

# Example usage:
if __name__ == "__main__":
    # Define a sample graph as an adjacency list
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('C', 1), ('D', 7)],
        'C': [('D', 3)],
        'D': [],
    }

    start_node = 'A'
    shortest_distances = spfa(graph, start_node)

    for node, distance in shortest_distances.items():
        print(f'Shortest distance from {start_node} to {node} is {distance}')
