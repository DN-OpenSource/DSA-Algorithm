"""BFS and DFS traversals + BFS shortest path on an unweighted graph."""

from collections import defaultdict, deque


def build(edges, directed=False):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g


def bfs(g, start):
    seen = {start}
    order = []
    q = deque([start])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return order


def dfs(g, start):
    seen = set()
    order = []

    def walk(u):
        seen.add(u)
        order.append(u)
        for v in g[u]:
            if v not in seen:
                walk(v)

    walk(start)
    return order


def shortest_path(g, src, dst):
    if src == dst:
        return [src]
    prev = {src: None}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in prev:
                prev[v] = u
                if v == dst:
                    path = [v]
                    while prev[path[-1]] is not None:
                        path.append(prev[path[-1]])
                    return path[::-1]
                q.append(v)
    return None


if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    g = build(edges)
    print("bfs from 1:", bfs(g, 1))
    print("dfs from 1:", dfs(g, 1))
    print("shortest 1->5:", shortest_path(g, 1, 5))
