from collections import defaultdict
import sys

def main():
    n, m = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    result = []

    def dfs(a):
        visited[a] = True
        for b in graph[a]:
            if not visited[b]:
                result.append((a, b))
                dfs(b)

    dfs(1)

    for a, b in result:
        print(a, b)

if __name__ == "__main__":
    main()