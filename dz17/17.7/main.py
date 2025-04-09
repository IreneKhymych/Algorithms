class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def insert(self, val):
        self.head = self._insert(self.head, val)

    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node

    def same(self, other):
        return self._same(self.head, other.head)

    def _same(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return (node1.val == node2.val and
                    self._same(node1.left, node2.left) and
                    self._same(node1.right, node2.right))
        return False

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

tree1 = Tree()
for val in arr1:
    tree1.insert(val)

tree2 = Tree()
for val in arr2:
    tree2.insert(val)

print(1 if tree1.same(tree2) else 0)
