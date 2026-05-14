"""Common code patterns next to their Big-O label.
Read each function and predict its Big-O before peeking at the comment.
"""


def first(arr):                       # O(1)
    return arr[0]


def sum_all(arr):                     # O(n)
    s = 0
    for x in arr:
        s += x
    return s


def has_duplicate_slow(arr):          # O(n^2)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


def has_duplicate_fast(arr):          # O(n) using a hash set
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False


def count_digits(n):                  # O(log n) -- n shrinks by /10 each step
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c


def all_pairs(arr):                   # O(n^2)
    out = []
    for a in arr:
        for b in arr:
            out.append((a, b))
    return out


def all_subsets(arr):                 # O(2^n)
    out = [[]]
    for x in arr:
        out += [s + [x] for s in out]
    return out


if __name__ == "__main__":
    print("first:           ", first([10, 20, 30]))
    print("sum_all:         ", sum_all([1, 2, 3, 4]))
    print("dup_slow:        ", has_duplicate_slow([1, 2, 3, 2]))
    print("dup_fast:        ", has_duplicate_fast([1, 2, 3, 2]))
    print("count_digits:    ", count_digits(12345))
    print("all_pairs 3:     ", all_pairs([1, 2, 3]))
    print("all_subsets 3:   ", all_subsets([1, 2, 3]))
