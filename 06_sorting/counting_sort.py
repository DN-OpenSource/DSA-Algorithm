"""Counting sort — O(n+k). Only works for integer keys with a small range k.
Beats O(n log n) when k is small."""


def counting_sort(a):
    if not a:
        return []
    lo, hi = min(a), max(a)
    counts = [0] * (hi - lo + 1)
    for x in a:
        counts[x - lo] += 1
    out = []
    for v, c in enumerate(counts):
        out.extend([v + lo] * c)
    return out


def radix_sort(a):
    """LSD radix sort for non-negative integers. O(d*(n+10)) = O(n)."""
    if not a:
        return []
    a = a[:]
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a:
            buckets[(x // exp) % 10].append(x)
        a = [x for b in buckets for x in b]
        exp *= 10
    return a


if __name__ == "__main__":
    print("counting:", counting_sort([4, 2, 2, 8, 3, 3, 1]))
    print("counting neg:", counting_sort([-3, -1, 0, 2, -2, 1]))
    print("radix:   ", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
