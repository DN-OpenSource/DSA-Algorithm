"""Iterative segment tree for range-sum + point update in O(log n)."""


class SegTree:
    def __init__(self, arr):
        n = 1
        while n < len(arr):
            n *= 2
        self.n = n
        self.t = [0] * (2 * n)
        for i, v in enumerate(arr):
            self.t[n + i] = v
        for i in range(n - 1, 0, -1):
            self.t[i] = self.t[2 * i] + self.t[2 * i + 1]

    def update(self, i, val):
        i += self.n
        self.t[i] = val
        i //= 2
        while i:
            self.t[i] = self.t[2 * i] + self.t[2 * i + 1]
            i //= 2

    def query(self, l, r):     # inclusive l..r
        res = 0
        l += self.n; r += self.n + 1
        while l < r:
            if l & 1: res += self.t[l]; l += 1
            if r & 1: r -= 1; res += self.t[r]
            l //= 2; r //= 2
        return res


if __name__ == "__main__":
    st = SegTree([1, 3, 5, 7, 9, 11])
    print("sum [1..3]:", st.query(1, 3))    # 3+5+7=15
    st.update(1, 10)
    print("sum [1..3] after update:", st.query(1, 3))   # 10+5+7=22
