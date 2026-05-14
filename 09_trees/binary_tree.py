"""Binary tree node + the four classic traversals."""

from collections import deque


class TreeNode:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right


def preorder(node, out=None):
    if out is None: out = []
    if node:
        out.append(node.v)
        preorder(node.left, out)
        preorder(node.right, out)
    return out


def inorder(node, out=None):
    if out is None: out = []
    if node:
        inorder(node.left, out)
        out.append(node.v)
        inorder(node.right, out)
    return out


def postorder(node, out=None):
    if out is None: out = []
    if node:
        postorder(node.left, out)
        postorder(node.right, out)
        out.append(node.v)
    return out


def level_order(root):
    out = []
    if not root:
        return out
    q = deque([root])
    while q:
        node = q.popleft()
        out.append(node.v)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return out


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameter(root):
    """Longest path between any two nodes (in edges). O(n)."""
    best = [0]

    def _h(node):
        if node is None:
            return 0
        l, r = _h(node.left), _h(node.right)
        best[0] = max(best[0], l + r)
        return 1 + max(l, r)

    _h(root)
    return best[0]


def is_balanced(root):
    """True if no subtree height differs by more than 1. O(n)."""
    def _check(node):
        if node is None:
            return 0
        l = _check(node.left)
        if l == -1:
            return -1
        r = _check(node.right)
        if r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)

    return _check(root) != -1


def lowest_common_ancestor(root, p, q):
    """LCA of nodes with values p and q in a binary tree. O(n)."""
    if root is None or root.v == p or root.v == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, None, TreeNode(6)))
    print("preorder :", preorder(root))
    print("inorder  :", inorder(root))
    print("postorder:", postorder(root))
    print("level    :", level_order(root))
    print("height   :", height(root))
    print("diameter :", diameter(root))
    print("balanced :", is_balanced(root))
    lca = lowest_common_ancestor(root, 4, 5)
    print("lca(4,5) :", lca.v if lca else None)   # 2
