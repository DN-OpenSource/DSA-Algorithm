"""Graph as adjacency list + connected components."""

from collections import defaultdict, deque


class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, w=1):
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    def nodes(self):
        return list(self.adj.keys())


def connected_components(g):
    seen = set()
    comps = []
    for start in g.nodes():
        if start in seen:
            continue
        comp = []
        q = deque([start]); seen.add(start)
        while q:
            u = q.popleft()
            comp.append(u)
            for v, _ in g.adj[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
        comps.append(comp)
    return comps


if __name__ == "__main__":
    g = Graph()
    for u, v in [(1, 2), (2, 3), (4, 5), (6, 6)]:
        g.add_edge(u, v)
    print("components:", connected_components(g))
