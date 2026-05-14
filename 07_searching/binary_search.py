"""Linear search, classic binary search, lower-bound, sqrt by bsearch."""


def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(arr, target):
    """Smallest index i such that arr[i] >= target. Returns len(arr) if none."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr, target):
    """Smallest index i such that arr[i] > target. Returns len(arr) if none."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def ternary_search_max(f, lo, hi, eps=1e-9):
    """Find x in [lo, hi] that maximises unimodal f. Returns x."""
    while hi - lo > eps:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            lo = m1
        else:
            hi = m2
    return (lo + hi) / 2


def int_sqrt(n):
    """floor(sqrt(n)) using binary search. No floats."""
    if n < 2:
        return n
    lo, hi = 1, n // 2
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return best


if __name__ == "__main__":
    a = [1, 3, 5, 7, 9, 11, 13]
    print("linear  9:", linear_search(a, 9))
    print("binary  9:", binary_search(a, 9))
    print("lower_b 6:", lower_bound(a, 6))           # 3 (first >=6 is 7)
    print("upper_b 7:", upper_bound(a, 7))           # 4 (first >7 is 9)
    print("ternary max -(x-3)^2:", round(ternary_search_max(lambda x: -(x-3)**2, 0, 10), 6))  # ~3.0
    print("int_sqrt 26:", int_sqrt(26))              # 5
