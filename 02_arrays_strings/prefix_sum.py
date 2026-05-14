"""Prefix sums: O(1) range sums after O(n) preprocessing."""


class PrefixSum:
    def __init__(self, arr):
        self.pre = [0] * (len(arr) + 1)
        for i, v in enumerate(arr):
            self.pre[i + 1] = self.pre[i] + v

    def range_sum(self, l, r):       # inclusive l..r
        return self.pre[r + 1] - self.pre[l]


def subarray_sum_equals_k(arr, k):
    """Count subarrays whose sum equals k (works with negatives)."""
    counts = {0: 1}
    total = 0
    answer = 0
    for x in arr:
        total += x
        answer += counts.get(total - k, 0)
        counts[total] = counts.get(total, 0) + 1
    return answer


if __name__ == "__main__":
    ps = PrefixSum([3, 1, 4, 1, 5, 9, 2, 6])
    print("sum [2..5]:", ps.range_sum(2, 5))      # 4+1+5+9 = 19
    print("count subarrays sum=5:", subarray_sum_equals_k([1, 2, 3, -2, 5], 5))
