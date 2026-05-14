"""Huffman coding -- the classic compression algorithm.
Greedy: always merge the two least-frequent symbols."""

import heapq
from collections import Counter


class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq; self.char = char
        self.left = left; self.right = right
    def __lt__(self, other): return self.freq < other.freq


def huffman_codes(text):
    freq = Counter(text)
    heap = [Node(f, c) for c, f in freq.items()]
    heapq.heapify(heap)
    if len(heap) == 1:
        only = heapq.heappop(heap)
        return {only.char: "0"}
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, Node(a.freq + b.freq, None, a, b))
    root = heap[0]

    codes = {}
    def walk(n, path):
        if n.char is not None:
            codes[n.char] = path or "0"
            return
        walk(n.left, path + "0")
        walk(n.right, path + "1")
    walk(root, "")
    return codes


def encode(text):
    codes = huffman_codes(text)
    return ''.join(codes[c] for c in text), codes


if __name__ == "__main__":
    bits, codes = encode("beep boop beer!")
    print("codes:", codes)
    print("bits :", bits)
    print(f"raw  : {len('beep boop beer!') * 8} bits ; huffman: {len(bits)} bits")
