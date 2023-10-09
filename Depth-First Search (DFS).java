import java.util.ArrayList;
import java.util.List;

class Graph {
    private int V; // Number of vertices
    private List<List<Integer>> adj; // Adjacency list representation

    public Graph(int V) {
        this.V = V;
        adj = new ArrayList<>(V);
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
    }

    public void addEdge(int v, int w) {
        adj.get(v).add(w);
    }

    // Recursive DFS function
    private void DFSUtil(int v, boolean[] visited) {
        visited[v] = true;
        System.out.print(v + " ");

        for (Integer neighbor : adj.get(v)) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited);
            }
        }
    }

    public void DFS(int v) {
        boolean[] visited = new boolean[V];
        DFSUtil(v, visited);
    }

    public static void main(String[] args) {
        Graph g = new Graph(5); // Create a graph with 5 vertices

        // Add edges
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);

        System.out.print("DFS starting from vertex 0: ");
        g.DFS(0);
    }
}
