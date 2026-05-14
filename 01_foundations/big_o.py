"""Empirically watch O(n) vs O(n^2) vs O(log n) as n grows."""

import time


def constant_op(arr):
    return arr[0] if arr else None            # O(1)


def linear_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total                              # O(n)


def quadratic_pairs(arr):
    pairs = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == 0:
                pairs += 1
    return pairs                              # O(n^2)


def binary_search(arr, target):               # arr must be sorted
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1                                 # O(log n)


def nlogn_sort(arr):
    return sorted(arr)                             # O(n log n) — Timsort


def time_it(fn, *args):
    start = time.perf_counter()
    fn(*args)
    return time.perf_counter() - start


if __name__ == "__main__":
    for n in (1_000, 5_000, 10_000):
        data = list(range(n))
        print(f"n = {n:>6}")
        print(f"  O(1)       constant_op    : {time_it(constant_op, data):.6f}s")
        print(f"  O(log n)   binary_search  : {time_it(binary_search, data, -1):.6f}s")
        print(f"  O(n)       linear_sum     : {time_it(linear_sum, data):.6f}s")
        print(f"  O(n log n) nlogn_sort     : {time_it(nlogn_sort, data):.6f}s")
        print(f"  O(n^2)     quadratic_pairs: {time_it(quadratic_pairs, data):.6f}s")
