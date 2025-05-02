from collections import defaultdict, deque
import sys

def topological_sort(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != n:
        return [-1]
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))

    result = topological_sort(n, edges)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
