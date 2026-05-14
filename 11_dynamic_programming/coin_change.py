"""Coin change: fewest coins to make `amount`. -1 if impossible."""


def coin_change(coins, amount):
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == INF else dp[amount]


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))      # 3 (5+5+1)
    print(coin_change([2], 3))             # -1
