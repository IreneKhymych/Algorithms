class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}

    def path(self, path_parts):
        if not path_parts:
            return
        first, *rest = path_parts
        if first not in self.subdirectories:
            self.subdirectories[first] = Directory(first)
        self.subdirectories[first].path(rest)

    def tree(self, depth=0):
        if depth > 0:
            print(" " * (depth - 1) + self.name)
        for subdir in sorted(self.subdirectories):
            self.subdirectories[subdir].tree(depth + 1)

def build_directory(paths):
    root = Directory("")
    for path in paths:
        path_parts = path.split("\\")
        root.path(path_parts)
    return root

def main():
    n = int(input())
    paths = [input().strip() for _ in range(n)]

    tree = build_directory(paths)
    for subdir in sorted(tree.subdirectories):
        tree.subdirectories[subdir].tree(1)

if __name__ == "__main__":
    main()
