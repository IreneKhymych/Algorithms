from collections import defaultdict, deque
import sys

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    component = [start]

    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)
                component.append(u)

    return component

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    components = []

    for v in range(1, n + 1):
        if not visited[v]:
            component = bfs(v, graph, visited)
            components.append(component)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(" ".join(map(str, comp)))

if __name__ == "__main__":
    main()
