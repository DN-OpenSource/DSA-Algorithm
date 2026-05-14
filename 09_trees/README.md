# Module 9 — Trees

## Theory

A **tree** is a connected, acyclic graph. We pick a **root** and every node
has zero or more **children**. The depth/height grow downward.

Special trees:

* **Binary tree** — each node has at most two children.
* **Binary search tree (BST)** — for every node, left subtree < node <
  right subtree. Gives O(log n) search/insert/delete *if balanced*.
* **Balanced BST** (AVL, Red-Black) — height stays O(log n) automatically.
* **Heap** — complete binary tree where parent ≤ children (min-heap) or
  parent ≥ children (max-heap). Stored in an array.
* **Trie** — tree of characters for string lookup (covered in module 14).

## Traversals on a binary tree

* **Preorder**:  node → left → right
* **Inorder**:   left → node → right  (gives sorted order on a BST)
* **Postorder**: left → right → node
* **Level-order (BFS)**: visit by depth using a queue.

## Worked example: insert into a BST

Insert 5, 3, 7, 4, 1 into an empty BST.
After 5: just root 5.
After 3: 3 < 5 → left of 5.
After 7: 7 > 5 → right of 5.
After 4: 4 < 5 → left; 4 > 3 → right of 3.
After 1: 1 < 5 → left; 1 < 3 → left of 3.

```
        5
       / \
      3   7
     / \
    1   4
```

Inorder traversal → 1, 3, 4, 5, 7  (sorted).

## Heap as an array

Index 0 = root. Children of `i` are at `2i+1` and `2i+2`. Parent of `i` is at
`(i-1)//2`. That's how Python's `heapq` works.

## Run

```
python3 dsa_course/09_trees/binary_tree.py
python3 dsa_course/09_trees/bst.py
python3 dsa_course/09_trees/heap.py
```
