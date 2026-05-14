# Module 10 — Graphs

## Theory

A **graph** is a set of **nodes (vertices)** connected by **edges**.

* **Directed** vs **undirected**: edges have direction or not.
* **Weighted** vs **unweighted**: edges carry numbers (distances, costs)?
* **Cyclic** vs **acyclic** (DAG = Directed Acyclic Graph).

Two ways to store:

* **Adjacency list** — `adj[u] = [v1, v2, ...]`. Best for sparse graphs.
* **Adjacency matrix** — `m[u][v] = 1/0` or weight. Best for dense graphs.

## The big four algorithms

| Algorithm   | Solves                                | Time            |
|-------------|---------------------------------------|-----------------|
| BFS         | shortest path in unweighted graph     | O(V + E)        |
| DFS         | connectivity, cycles, topo sort       | O(V + E)        |
| Dijkstra    | shortest path with non-negative weights| O((V+E) log V) |
| Kruskal/Prim| minimum spanning tree (MST)           | O(E log V)      |

## Mental picture

* **BFS** = ripples in a pond. Use a queue; visit nodes layer by layer.
* **DFS** = exploring a maze with a torch — go deep, backtrack at dead ends.
* **Dijkstra** = BFS but the queue is a min-heap by distance.

## Worked example: BFS shortest path

Graph (undirected): 1-2, 1-3, 2-4, 3-4, 4-5. Start 1.
Queue: [1]. dist: {1:0}.
Pop 1 → enqueue 2, 3 with dist 1.
Pop 2 → enqueue 4 with dist 2.
Pop 3 → 4 already seen.
Pop 4 → enqueue 5 with dist 3.
Pop 5 → done. Shortest path 1→5 has length 3.

## Run

```
python3 dsa_course/10_graphs/graph_basics.py
python3 dsa_course/10_graphs/bfs_dfs.py
python3 dsa_course/10_graphs/dijkstra.py
python3 dsa_course/10_graphs/topo_sort.py
```
