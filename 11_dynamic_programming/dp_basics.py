"""Climbing stairs, house robber, fib bottom-up."""


def fib(n):
    if n < 2: return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def house_robber(nums):
    prev = curr = 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr


def longest_increasing_subsequence(nums):
    """Length of LIS. O(n log n) via patience sorting."""
    import bisect
    tails = []
    for x in nums:
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)


if __name__ == "__main__":
    print("fib(20):", fib(20))
    print("stairs(6):", climb_stairs(6))
    print("robber [2,7,9,3,1]:", house_robber([2, 7, 9, 3, 1]))
    print("LIS [10,9,2,5,3,7,101,18]:", longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
