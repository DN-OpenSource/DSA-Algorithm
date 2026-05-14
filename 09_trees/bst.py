"""Binary Search Tree: insert, search, delete, in-order iteration."""


class BSTNode:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, v):
        self.root = self._insert(self.root, v)

    def _insert(self, node, v):
        if node is None:
            return BSTNode(v)
        if v < node.v:
            node.left = self._insert(node.left, v)
        elif v > node.v:
            node.right = self._insert(node.right, v)
        return node

    def contains(self, v):
        node = self.root
        while node:
            if v == node.v: return True
            node = node.left if v < node.v else node.right
        return False

    def delete(self, v):
        self.root = self._delete(self.root, v)

    def _delete(self, node, v):
        if node is None:
            return None
        if v < node.v:
            node.left = self._delete(node.left, v)
        elif v > node.v:
            node.right = self._delete(node.right, v)
        else:
            if node.left is None:  return node.right
            if node.right is None: return node.left
            succ = node.right                       # in-order successor
            while succ.left:
                succ = succ.left
            node.v = succ.v
            node.right = self._delete(node.right, succ.v)
        return node

    def min_val(self):
        node = self.root
        while node and node.left:
            node = node.left
        return node.v if node else None

    def max_val(self):
        node = self.root
        while node and node.right:
            node = node.right
        return node.v if node else None

    def floor(self, v):
        """Largest value <= v in the BST."""
        res, node = None, self.root
        while node:
            if node.v == v:
                return v
            if node.v < v:
                res = node.v
                node = node.right
            else:
                node = node.left
        return res

    def ceil(self, v):
        """Smallest value >= v in the BST."""
        res, node = None, self.root
        while node:
            if node.v == v:
                return v
            if node.v > v:
                res = node.v
                node = node.left
            else:
                node = node.right
        return res

    def inorder(self):
        out = []
        def walk(n):
            if n:
                walk(n.left); out.append(n.v); walk(n.right)
        walk(self.root)
        return out


if __name__ == "__main__":
    t = BST()
    for x in [5, 3, 7, 4, 1, 9, 2]:
        t.insert(x)
    print("inorder:", t.inorder())
    print("contains 4:", t.contains(4))
    print("min:", t.min_val(), " max:", t.max_val())
    print("floor(6):", t.floor(6), " ceil(6):", t.ceil(6))
    t.delete(3)
    print("after delete 3:", t.inorder())
