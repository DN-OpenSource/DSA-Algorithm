"""Min-heap from scratch + usage of Python's heapq for top-k."""

import heapq


class MinHeap:
    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)
        self._sift_up(len(self.a) - 1)

    def pop(self):
        if not self.a:
            return None
        top = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            self._sift_down(0)
        return top

    def peek(self):
        return self.a[0] if self.a else None

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.a[i] < self.a[parent]:
                self.a[i], self.a[parent] = self.a[parent], self.a[i]
                i = parent
            else:
                return

    def _sift_down(self, i):
        n = len(self.a)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i
            if l < n and self.a[l] < self.a[smallest]: smallest = l
            if r < n and self.a[r] < self.a[smallest]: smallest = r
            if smallest == i:
                return
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            i = smallest


def k_smallest(nums, k):
    """Top-k smallest using a heap. O(n log k)."""
    heap = []                                   # max-heap by negation
    for x in nums:
        heapq.heappush(heap, -x)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(-x for x in heap)


if __name__ == "__main__":
    h = MinHeap()
    for x in [5, 2, 9, 1, 6, 3]:
        h.push(x)
    print("pops:", [h.pop() for _ in range(6)])
    print("k=3 smallest:", k_smallest([5, 2, 9, 1, 6, 3, 8, 0], 3))
