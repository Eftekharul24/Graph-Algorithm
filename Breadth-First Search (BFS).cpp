#include <iostream>
#include <list>
#include <queue>

class Graph {
    int numVertices; // Number of vertices
    std::list<int>* adjLists; // Adjacency lists

public:
    Graph(int vertices); // Constructor
    void addEdge(int src, int dest); // Add an edge to the graph
    void BFS(int startVertex); // Breadth-First Search
};

// Constructor
Graph::Graph(int vertices) {
    numVertices = vertices;
    adjLists = new std::list<int>[vertices];
}

// Add an edge to the graph
void Graph::addEdge(int src, int dest) {
    adjLists[src].push_back(dest);
    adjLists[dest].push_back(src); // For undirected graph
}

// Breadth-First Search
void Graph::BFS(int startVertex) {
    bool* visited = new bool[numVertices];
    for (int i = 0; i < numVertices; i++) {
        visited[i] = false;
    }

    std::queue<int> queue;
    visited[startVertex] = true;
    queue.push(startVertex);

    std::cout << "Breadth-First Traversal starting from vertex " << startVertex << ":\n";

    while (!queue.empty()) {
        int currentVertex = queue.front();
        std::cout << "Visited vertex: " << currentVertex << std::endl;
        queue.pop();

        for (int neighbor : adjLists[currentVertex]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.push(neighbor);
            }
        }
    }

    delete[] visited;
}

int main() {
    int numVertices = 6; // Change this as needed
    Graph graph(numVertices);

    graph.addEdge(0, 1);
    graph.addEdge(0, 2);
    graph.addEdge(1, 3);
    graph.addEdge(2, 4);
    graph.addEdge(3, 5);

    graph.BFS(0);

    return 0;
}
