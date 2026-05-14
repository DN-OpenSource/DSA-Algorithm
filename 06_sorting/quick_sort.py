"""Quicksort — partition then recurse. Lomuto + random pivot for safety."""

import random


def quick_sort(a):
    a = a[:]
    _qs(a, 0, len(a) - 1)
    return a


def _qs(a, lo, hi):
    if lo >= hi:
        return
    p = _partition(a, lo, hi)
    _qs(a, lo, p - 1)
    _qs(a, p + 1, hi)


def _partition(a, lo, hi):
    pivot_index = random.randint(lo, hi)
    a[pivot_index], a[hi] = a[hi], a[pivot_index]
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


if __name__ == "__main__":
    print(quick_sort([5, 2, 4, 6, 1, 3, 3, 7, 0]))
