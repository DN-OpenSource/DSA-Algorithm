# Module 6 — Sorting

## Theory

Sorting is everywhere because once data is sorted, many problems become
easy (binary search, deduping, range queries, greedy choices).

| Algorithm       | Time avg     | Time worst | Space   | Stable | Notes                          |
|-----------------|--------------|------------|---------|--------|--------------------------------|
| Bubble sort     | O(n^2)       | O(n^2)     | O(1)    | yes    | teaching only                  |
| Insertion sort  | O(n^2)       | O(n^2)     | O(1)    | yes    | great for nearly-sorted        |
| Selection sort  | O(n^2)       | O(n^2)     | O(1)    | no     | minimum-swap                   |
| Merge sort      | O(n log n)   | O(n log n) | O(n)    | yes    | divide & conquer; external sort|
| Quick sort      | O(n log n)   | O(n^2)     | O(log n)| no     | fastest in practice            |
| Heap sort       | O(n log n)   | O(n log n) | O(1)    | no     | uses a heap                    |
| Counting sort   | O(n + k)     | O(n + k)   | O(k)    | yes    | only for small-int keys        |

`stable` = elements with equal keys keep their original order.

## Worked example: merge sort

`[5, 2, 4, 6, 1, 3]`
split → `[5,2,4]` and `[6,1,3]`
split each → `[5][2,4]`, `[6][1,3]`
sort the pairs → `[2,4]`, `[1,3]`
merge `[5]` and `[2,4]` → `[2,4,5]`
merge `[6]` and `[1,3]` → `[1,3,6]`
merge `[2,4,5]` and `[1,3,6]` → `[1,2,3,4,5,6]`.

## Run

```
python3 dsa_course/06_sorting/elementary_sorts.py
python3 dsa_course/06_sorting/merge_sort.py
python3 dsa_course/06_sorting/quick_sort.py
python3 dsa_course/06_sorting/heap_sort.py
python3 dsa_course/06_sorting/counting_sort.py
```
