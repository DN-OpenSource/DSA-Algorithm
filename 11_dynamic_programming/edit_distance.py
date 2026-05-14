"""Edit distance (Levenshtein) -- min operations to transform string a -> b.
Operations: insert, delete, replace (each costs 1).
Classic DP used in spell-checkers, diff tools, DNA alignment."""


def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            temp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = temp
    return dp[m]


if __name__ == "__main__":
    print(edit_distance("kitten", "sitting"))   # 3
    print(edit_distance("sunday", "saturday"))  # 3
    print(edit_distance("", "abc"))             # 3
    print(edit_distance("abc", "abc"))          # 0
