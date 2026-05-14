# Module 14 — Advanced Structures

These are the tools you reach for after the basics are second nature.

## 1. Trie (prefix tree)

A tree where every edge is a character. Looking up a word of length L is
O(L), independent of how many words are stored. Used for autocomplete,
spell-check, IP routing, and reading large dictionaries.

## 2. Union-Find / Disjoint Set Union (DSU)

A data structure to keep a forest of sets and support:
* `find(x)` — which set does x belong to?
* `union(a, b)` — merge the two sets.

Both operations are *almost* O(1) (amortized α(n)) with the two
optimizations **path compression** and **union by rank**. Used for:
Kruskal's MST, network connectivity, cycle detection in undirected graphs.

## 3. Segment Tree

A binary tree over an array that supports
* point updates and range queries (sum/min/max) in O(log n).
Used in competitive programming, range databases, mutable interval queries.

## 4. Fenwick tree / BIT (mentioned only)

Lighter than a segment tree, supports prefix-sum + point updates in
O(log n). Smaller constants.

## Worked example: Union-Find on Kruskal

To build a minimum spanning tree (MST):
  1. Sort all edges by weight.
  2. Walk through edges; for each, if its two endpoints are in different
     sets, take the edge and `union` them.
  3. Stop when V-1 edges chosen.

## Run

```
python3 dsa_course/14_advanced/trie.py
python3 dsa_course/14_advanced/union_find.py
python3 dsa_course/14_advanced/segment_tree.py
```
