"""0/1 Knapsack — pick items to maximize value within weight budget."""


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if w <= c:
                dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)
    return dp[n][capacity]


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    print(knapsack(weights, values, 5))      # 7  (items 1+2)
