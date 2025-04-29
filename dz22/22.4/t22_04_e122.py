from collections import defaultdict
import sys
sys.setrecursionlimit(10000) 

def gr():
    n, a, b, d = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(n):
        u, v = map(int, input().split())
        graph[u].append(v)

    count = 0

    def dfs(node, depth, visited):
        nonlocal count
        if depth > d:
            return
        if node == b and depth > 0:
            count += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, depth + 1, visited | {neighbor})

    dfs(a, 0, {a})
    print(count)

if __name__ == "__main__":
    gr()
