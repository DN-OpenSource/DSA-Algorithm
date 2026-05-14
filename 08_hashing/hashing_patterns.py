"""Classic hash-map patterns: two-sum, anagram groups, frequency."""

from collections import Counter, defaultdict


def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        seen[x] = i
    return None


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        groups[key].append(w)
    return list(groups.values())


def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [val for val, _ in freq.most_common(k)]


def first_unique_char(s):
    freq = Counter(s)
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1


if __name__ == "__main__":
    print("two_sum:", two_sum([2, 7, 11, 15], 9))
    print("anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("top 2:", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print("first unique 'leetcode':", first_unique_char("leetcode"))
