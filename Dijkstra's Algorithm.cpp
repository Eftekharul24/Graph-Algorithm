#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

// Define a structure to represent an edge with weight
struct Edge {
    int target;
    int weight;
    Edge(int t, int w) : target(t), weight(w) {}
};

// Define a comparator for priority queue to select the vertex with the smallest distance
struct CompareDist {
    bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {
        return lhs.second > rhs.second;
    }
};

class Graph {
    int V; // Number of vertices
    vector<vector<Edge>> adj; // Adjacency list representation

public:
    Graph(int V); // Constructor
    void addEdge(int src, int target, int weight); // Add an edge to the graph
    void dijkstra(int src); // Dijkstra's algorithm to find shortest paths
};

Graph::Graph(int V) {
    this->V = V;
    adj.resize(V);
}

void Graph::addEdge(int src, int target, int weight) {
    adj[src].emplace_back(target, weight);
    adj[target].emplace_back(src, weight); // For an undirected graph, add the reverse edge as well
}

void Graph::dijkstra(int src) {
    vector<int> dist(V, numeric_limits<int>::max());
    dist[src] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, CompareDist> pq;
    pq.push(make_pair(src, 0));

    while (!pq.empty()) {
        int u = pq.top().first;
        pq.pop();

        for (const Edge& edge : adj[u]) {
            int v = edge.target;
            int weight = edge.weight;

            if (dist[u] != numeric_limits<int>::max() && dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push(make_pair(v, dist[v]));
            }
        }
    }

    // Print the shortest distances from the source vertex
    cout << "Vertex \t Distance from Source" << endl;
    for (int i = 0; i < V; i++) {
        cout << i << "\t" << dist[i] << endl;
    }
}

int main() {
    int V = 5; // Number of vertices
    Graph g(V);

    // Add edges with weights
    g.addEdge(0, 1, 4);
    g.addEdge(0, 2, 8);
    g.addEdge(1, 2, 1);
    g.addEdge(1, 3, 2);
    g.addEdge(2, 3, 5);
    g.addEdge(3, 4, 3);

    int source = 0; // Source vertex

    cout << "Shortest distances from vertex " << source << ":\n";
    g.dijkstra(source);

    return 0;
}
