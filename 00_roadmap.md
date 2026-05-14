# From Zero to AI — DSA & Algorithms Roadmap

This course takes you from "what is an algorithm?" to building a tiny neural
network from scratch. Every module follows the same pattern:

  1. Theory (the *why*, in plain English)
  2. Worked example (the *how*, by hand)
  3. Code (the *do*, runnable Python)

Language: Python 3 — chosen because it reads like pseudocode.

## Order of modules

| #  | Folder                       | Topic                              |
|----|------------------------------|------------------------------------|
| 1  | 01_foundations               | Big-O, memory, problem solving     |
| 2  | 02_arrays_strings            | Arrays, strings, two pointers      |
| 3  | 03_linked_lists              | Singly, doubly, circular           |
| 4  | 04_stacks_queues             | Stack, queue, deque, monotonic     |
| 5  | 05_recursion_backtracking    | Recursion, backtracking            |
| 6  | 06_sorting                   | Bubble, merge, quick, heap, counting, radix |
| 7  | 07_searching                 | Linear, binary (lower/upper bound), ternary |
| 8  | 08_hashing                   | Hash maps, sets, collisions        |
| 9  | 09_trees                     | BST, AVL, heap, traversals         |
| 10 | 10_graphs                    | BFS, DFS, Dijkstra, Bellman-Ford, MST, topo sort |
| 11 | 11_dynamic_programming       | Memoization, tabulation, LIS, edit distance, classics |
| 12 | 12_greedy                    | Greedy proofs and patterns         |
| 13 | 13_bit_and_math              | Bitwise tricks, number theory      |
| 14 | 14_advanced                  | Trie, segment tree, union-find     |
| 15 | 15_bridge_to_ai              | Vectors, kNN, gradient descent, NN |

## How to study

* Read the README, do the example **by hand on paper**, *then* run the code.
* Modify the code (break it!). Understanding survives only what you change.
* After each module solve 5–10 LeetCode/Codeforces problems on the topic.

## How to run the code

```
python3 dsa_course/01_foundations/big_o.py
```

Every file has a `if __name__ == "__main__":` demo so you can run it directly.
