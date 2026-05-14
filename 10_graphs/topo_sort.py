"""Topological sort of a DAG (Kahn's algorithm).
Used for task scheduling, build systems, course prerequisites."""

from collections import defaultdict, deque


def topo_sort(n, edges):
    """n = number of nodes 0..n-1. edges = [(u,v)] means u must come before v."""
    indeg = [0] * n
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else None    # None => cycle


def topo_sort_dfs(n, edges):
    """DFS-based topological sort. Returns None if cycle detected."""
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    order = []
    has_cycle = [False]

    def dfs(u):
        color[u] = GRAY
        for v in g[u]:
            if color[v] == GRAY:
                has_cycle[0] = True
                return
            if color[v] == WHITE:
                dfs(v)
                if has_cycle[0]:
                    return
        color[u] = BLACK
        order.append(u)

    for i in range(n):
        if color[i] == WHITE:
            dfs(i)
            if has_cycle[0]:
                return None
    return order[::-1]


if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    print("kahn :", topo_sort(5, edges))
    print("dfs  :", topo_sort_dfs(5, edges))
