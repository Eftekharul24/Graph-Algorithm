#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Define the maximum number of vertices
#define MAX_VERTICES 100

// Define a structure for a node in the adjacency list
struct Node {
    int data;
    struct Node* next;
};

// Define a structure for the adjacency list
struct Graph {
    int numVertices;
    struct Node* adjLists[MAX_VERTICES];
    int visited[MAX_VERTICES];
};

// Create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Create a graph with a given number of vertices
struct Graph* createGraph(int vertices) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = vertices;

    for (int i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL;
        graph->visited[i] = 0;
    }

    return graph;
}

// Add an edge to the graph
void addEdge(struct Graph* graph, int src, int dest) {
    // Add edge from src to dest
    struct Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;

    // Add edge from dest to src (for undirected graph)
    newNode = createNode(src);
    newNode->next = graph->adjLists[dest];
    graph->adjLists[dest] = newNode;
}

// Breadth-First Search function
void BFS(struct Graph* graph, int startVertex) {
    int queue[MAX_VERTICES];
    int front = -1, rear = -1;

    graph->visited[startVertex] = 1;
    queue[++rear] = startVertex;

    printf("Breadth-First Traversal starting from vertex %d:\n", startVertex);

    while (front < rear) {
        int currentVertex = queue[++front];
        printf("Visited vertex: %d\n", currentVertex);

        struct Node* temp = graph->adjLists[currentVertex];
        while (temp) {
            int adjVertex = temp->data;
            if (graph->visited[adjVertex] == 0) {
                graph->visited[adjVertex] = 1;
                queue[++rear] = adjVertex;
            }
            temp = temp->next;
        }
    }
}

int main() {
    int numVertices = 6; // Change this as needed
    struct Graph* graph = createGraph(numVertices);

    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 2, 4);
    addEdge(graph, 3, 5);

    BFS(graph, 0);

    return 0;
}
