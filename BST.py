class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        res = []
        if node:
            res = self._inorder(node.left)
            res.append(node.key)
            res += self._inorder(node.right)
        return res


if __name__ == "__main__":
    bst = BST()
    keys = [50, 30, 20, 40, 70, 60, 80]
    for key in keys:
        bst.insert(key)
    print("Inorder traversal:", bst.inorder())
