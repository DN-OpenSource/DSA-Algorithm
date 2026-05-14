"""Heap sort: build a max-heap in place, then repeatedly extract."""


def heap_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):     # build max-heap
        _sift_down(a, i, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        _sift_down(a, 0, end)
    return a


def _sift_down(a, i, n):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        biggest = i
        if left < n and a[left] > a[biggest]:
            biggest = left
        if right < n and a[right] > a[biggest]:
            biggest = right
        if biggest == i:
            return
        a[i], a[biggest] = a[biggest], a[i]
        i = biggest


if __name__ == "__main__":
    print(heap_sort([5, 2, 4, 6, 1, 3]))
