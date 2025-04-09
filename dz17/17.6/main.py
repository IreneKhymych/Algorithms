class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(node):
    if not node:
        return ''
    return node.val + preorder(node.left) + preorder(node.right)

def insert(root, node):
    if not root:
        return node
    if node.val < root.val:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root

def tree(waves):
    root = None
    for level in reversed(waves):
        for val in level:
            node = Node(val)
            root = insert(root, node)
    return root

def main():
    import sys
    import os

    lines = []
    if os.path.exists("input.txt"):
        with open("input.txt") as f:
            for line in f:
                line = line.strip()
                if line == "*":
                    break
                lines.append(line)
    else:
        for line in sys.stdin:
            line = line.strip()
            if line == "*":
                break
            lines.append(line)

    waves = [list(line) for line in lines]
    root = tree(waves)
    print(preorder(root))

if __name__ == "__main__":
    main()