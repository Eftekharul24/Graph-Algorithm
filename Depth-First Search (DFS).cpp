#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Graph {
    int V; // Number of vertices

    // Adjacency list representation
    vector<vector<int>> adj;

    // Recursive DFS function
    void DFSUtil(int v, vector<bool>& visited);

public:
    Graph(int V); // Constructor
    void addEdge(int v, int w); // Add an edge to the graph
    void DFS(int v); // DFS traversal starting from vertex v
};

Graph::Graph(int V) {
    this->V = V;
    adj.resize(V);
}

void Graph::addEdge(int v, int w) {
    adj[v].push_back(w);
}

void Graph::DFSUtil(int v, vector<bool>& visited) {
    // Mark the current node as visited
    visited[v] = true;
    cout << v << " ";

    // Recur for all the adjacent vertices
    for (int i = 0; i < adj[v].size(); ++i) {
        int adjacentVertex = adj[v][i];
        if (!visited[adjacentVertex]) {
            DFSUtil(adjacentVertex, visited);
        }
    }
}

void Graph::DFS(int v) {
    // Create a boolean array to keep track of visited vertices
    vector<bool> visited(V, false);

    // Call the recursive helper function
    DFSUtil(v, visited);
}

int main() {
    Graph g(5); // Create a graph with 5 vertices

    // Add edges
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);

    cout << "DFS starting from vertex 0: ";
    g.DFS(0);

    return 0;
}
