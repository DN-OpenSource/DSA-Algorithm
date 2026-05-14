"""Trie — autocomplete in O(L) per word."""


class TrieNode:
    __slots__ = ("children", "is_word")
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.is_word = True

    def contains(self, word):
        node = self._walk(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def autocomplete(self, prefix, limit=10):
        out = []
        node = self._walk(prefix)
        if not node:
            return out

        def dfs(n, path):
            if len(out) == limit:
                return
            if n.is_word:
                out.append(prefix + path)
            for ch, child in n.children.items():
                dfs(child, path + ch)

        dfs(node, "")
        return out


if __name__ == "__main__":
    t = Trie()
    for w in ["car", "card", "care", "cargo", "dog", "do"]:
        t.insert(w)
    print("contains card:", t.contains("card"))
    print("starts car:", t.starts_with("car"))
    print("autocomplete 'ca':", t.autocomplete("ca"))
