# Module 12 — Greedy Algorithms

## Theory

A **greedy** algorithm builds an answer step by step, *each step making the
locally best choice*, hoping that the global optimum follows.

Greedy is fast and simple. The catch: it's not always correct. To trust a
greedy algorithm you need a **proof** (usually an "exchange argument" —
show that any non-greedy choice can be swapped for the greedy one without
losing optimality).

## When greedy works

* The problem has the **greedy choice property** (a globally optimal
  solution can be reached by local choices).
* And **optimal substructure** (an optimal solution contains optimal sub-
  solutions).

## Classic greedy problems

| Problem                          | Strategy                            |
|----------------------------------|-------------------------------------|
| Activity selection               | always pick the next activity that ends earliest |
| Coin change (canonical coin sets)| always take the largest coin <= amount |
| Huffman coding                   | always merge the two least-frequent nodes |
| Fractional knapsack              | sort by value/weight, take highest first |
| Minimum platforms / interval scheduling | sort by start, sweep with a heap |

Note: 0/1 knapsack is **not** solvable greedily — that's why we used DP.

## Worked example: activity selection

Activities (start, end): (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10),
(8,11), (8,12), (2,14), (12,16).
Sort by end time. Pick the first; then each next whose start ≥ previous end.

## Run

```
python3 dsa_course/12_greedy/activity_selection.py
python3 dsa_course/12_greedy/huffman.py
```
