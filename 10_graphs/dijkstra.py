"""Dijkstra's shortest path with a min-heap (priority queue)."""

import heapq
from collections import defaultdict


def dijkstra(edges, src):
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))                     # undirected; remove for directed

    dist = {src: 0}
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def bellman_ford(nodes, edges, src):
    """Shortest paths from src. Handles negative weights. O(V*E).
    Returns dist dict, or None if a negative cycle is reachable."""
    dist = {n: float('inf') for n in nodes}
    dist[src] = 0
    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None                         # negative cycle detected
    return dist


if __name__ == "__main__":
    edges = [
        ('A', 'B', 1), ('A', 'C', 4),
        ('B', 'C', 2), ('B', 'D', 5),
        ('C', 'D', 1),
    ]
    print("dijkstra:", dijkstra(edges, 'A'))        # {A:0, B:1, C:3, D:4}
    nodes = ['A', 'B', 'C', 'D']
    print("bellman :", bellman_ford(nodes, edges, 'A'))
