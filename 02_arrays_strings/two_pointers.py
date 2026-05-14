"""Two-pointer patterns: pair sum, palindrome, reverse, remove duplicates."""


def pair_sum_sorted(arr, target):
    """Return indices (l, r) such that arr[l] + arr[r] == target."""
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return (l, r)
        if s < target:
            l += 1
        else:
            r -= 1
    return None


def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def reverse_in_place(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


def remove_duplicates_sorted(arr):
    """In a sorted array, keep only first occurrence. Return new length."""
    if not arr:
        return 0
    w = 1
    for r in range(1, len(arr)):
        if arr[r] != arr[w - 1]:
            arr[w] = arr[r]
            w += 1
    return w


if __name__ == "__main__":
    print("pair_sum_sorted:", pair_sum_sorted([1, 3, 4, 6, 8, 11], 10))
    print("is_palindrome 'A man, a plan, a canal: Panama':",
          is_palindrome("A man, a plan, a canal: Panama"))
    print("reverse:", reverse_in_place([1, 2, 3, 4, 5]))
    arr = [1, 1, 2, 2, 3, 4, 4, 5]
    n = remove_duplicates_sorted(arr)
    print("dedup:", arr[:n])
