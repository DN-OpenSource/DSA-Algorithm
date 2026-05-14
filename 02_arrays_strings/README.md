# Module 2 — Arrays and Strings

## Theory

* **Array** = a contiguous block of memory holding items of (usually) the
  same type. Accessing `arr[i]` is O(1) because the CPU computes
  `address(arr) + i * size_of_item` and jumps there.
* **String** = an immutable array of characters (in Python). Slicing a string
  builds a new string.
* **Dynamic array** (Python `list`, C++ `vector`) doubles its capacity when
  full, so `append` is *amortized* O(1).

Operations:

| Op                       | Time   | Notes                              |
|--------------------------|--------|-------------------------------------|
| index access `a[i]`      | O(1)   |                                     |
| append `a.append(x)`     | O(1)*  | amortized                           |
| insert at front          | O(n)   | every element shifts                |
| delete at index          | O(n)   |                                     |
| search (unsorted)        | O(n)   |                                     |
| search (sorted)          | O(log n)| binary search                       |

## Key technique #1 — Two pointers

Walk two indices through the array. Great for sorted arrays, palindrome
checks, removing duplicates, "pair sums to target".

## Key technique #2 — Sliding window

Maintain a window `[L, R]` that satisfies some property; shrink/grow it.
Great for "longest substring with k distinct chars", "max sum of size k".

## Key technique #3 — Prefix sums

`pre[i] = arr[0] + arr[1] + ... + arr[i-1]`. Then any range sum
`arr[l..r] = pre[r+1] - pre[l]` in O(1).

## Worked example: two-sum on a sorted array

Array: `[1, 3, 4, 6, 8, 11]`, target = 10.
Pointers L=0 (val 1), R=5 (val 11). 1+11=12 > 10, move R left.
L=0, R=4: 1+8=9 < 10, move L right.
L=1, R=4: 3+8=11 > 10, R left.
L=1, R=3: 3+6=9 < 10, L right.
L=2, R=3: 4+6=10 → found.

## Run

```
python3 dsa_course/02_arrays_strings/two_pointers.py
python3 dsa_course/02_arrays_strings/sliding_window.py
python3 dsa_course/02_arrays_strings/prefix_sum.py
```
