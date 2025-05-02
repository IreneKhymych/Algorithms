from collections import defaultdict, deque
import sys

def connected(n, edges, removed_set):
    adj = defaultdict(list)
    for idx, (u, v) in enumerate(edges, 1):
        if idx not in removed_set:
            adj[u].append(v)
            adj[v].append(u)

    visited = set()
    queue = deque([1])
    visited.add(1)
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) == n

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0

    n = int(data[ptr])
    m = int(data[ptr + 1])
    ptr += 2

    edges = []
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        edges.append((u, v))
        ptr += 2

    k = int(data[ptr])
    ptr += 1

    results = []
    for _ in range(k):
        c = int(data[ptr])
        removed = set(int(data[ptr + i]) for i in range(1, c + 1))
        ptr += c + 1

        if connected(n, edges, removed):
            results.append("Connected")
        else:
            results.append("Disconnected")

    print("\n".join(results))

if __name__ == "__main__":
    main()
