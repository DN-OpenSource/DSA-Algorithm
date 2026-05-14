# Module 7 — Searching

## Theory

* **Linear search** — check each element. O(n). Works on any list.
* **Binary search** — only on a **sorted** list. Halve the search space
  each step. O(log n).
* **Ternary search** — for unimodal functions (one peak/valley), split into
  thirds. O(log n) but with a worse constant.

## When to *think* of binary search

Whenever the answer space is monotone (yes/no flips at exactly one point):
"smallest x such that condition(x) is true". That includes:

* finding a value in a sorted list
* sqrt(n) without floats
* "minimum capacity to ship packages in k days"
* "smallest day you can finish all tasks"

## Worked example: binary search

Sorted: `[1, 3, 5, 7, 9, 11, 13]`. Find 9.
lo=0, hi=6, mid=3 → 7. 7<9, lo=4.
lo=4, hi=6, mid=5 → 11. 11>9, hi=4.
lo=4, hi=4, mid=4 → 9. Found at index 4.

## Run

```
python3 dsa_course/07_searching/binary_search.py
```
