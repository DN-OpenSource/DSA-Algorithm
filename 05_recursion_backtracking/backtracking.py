"""Backtracking: permutations, subsets, N-Queens."""


def permutations(nums):
    out, cur, used = [], [], [False] * len(nums)

    def bt():
        if len(cur) == len(nums):
            out.append(cur[:])
            return
        for i, v in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            cur.append(v)
            bt()
            cur.pop()                # undo
            used[i] = False

    bt()
    return out


def subsets(nums):
    out, cur = [], []

    def bt(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            cur.append(nums[i])
            bt(i + 1)
            cur.pop()

    bt(0)
    return out


def n_queens(n):
    """Return the number of valid placements of n non-attacking queens."""
    cols = set(); diag1 = set(); diag2 = set()
    count = [0]

    def bt(row):
        if row == n:
            count[0] += 1
            return
        for c in range(n):
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue
            cols.add(c); diag1.add(row - c); diag2.add(row + c)
            bt(row + 1)
            cols.remove(c); diag1.remove(row - c); diag2.remove(row + c)

    bt(0)
    return count[0]


if __name__ == "__main__":
    print("perms [1,2,3]:", permutations([1, 2, 3]))
    print("subsets [1,2,3]:", subsets([1, 2, 3]))
    print("8-queens solutions:", n_queens(8))    # expected 92
