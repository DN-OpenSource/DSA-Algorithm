"""Union-Find with path compression + union by rank, plus Kruskal MST."""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.components -= 1
        return True


def kruskal(n, edges):
    """edges = list of (weight, u, v). Returns (total_weight, picked)."""
    uf = UnionFind(n)
    edges = sorted(edges)
    total = 0
    picked = []
    for w, u, v in edges:
        if uf.union(u, v):
            total += w
            picked.append((u, v, w))
            if len(picked) == n - 1:
                break
    return total, picked


if __name__ == "__main__":
    edges = [(1, 0, 1), (4, 0, 2), (2, 1, 2), (5, 1, 3), (1, 2, 3)]
    print(kruskal(4, edges))
