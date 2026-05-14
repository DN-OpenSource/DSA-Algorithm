"""Sliding window: max sum of k, longest substring without repeats."""


def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best


def longest_unique_substring(s):
    last_seen = {}
    l = 0
    best = 0
    for r, c in enumerate(s):
        if c in last_seen and last_seen[c] >= l:
            l = last_seen[c] + 1
        last_seen[c] = r
        best = max(best, r - l + 1)
    return best


def min_window_with_sum_atleast(arr, target):
    """Shortest contiguous subarray with sum >= target (positive nums)."""
    l = 0
    cur = 0
    best = float('inf')
    for r in range(len(arr)):
        cur += arr[r]
        while cur >= target:
            best = min(best, r - l + 1)
            cur -= arr[l]
            l += 1
    return 0 if best == float('inf') else best


if __name__ == "__main__":
    print("max_sum_subarray k=3:", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
    print("longest_unique 'abcabcbb':", longest_unique_substring("abcabcbb"))
    print("min_window sum>=7:", min_window_with_sum_atleast([2, 1, 5, 2, 3, 2], 7))
