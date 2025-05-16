n, m = map(int, input().split())
edges = []
INF = float('inf')

def Bellman_Ford(n, edges):
    dist = [INF] * (n + 1)
    dist[n] = 0
    all_edges = edges + [(n, i, 0) for i in range(n)]

    for i in range(n):
        updated = False
        for u, v, t in all_edges:
            if dist[u] + t < dist[v]:
                dist[v] = dist[u] + t
                updated = True
        if not updated:
            break
        if i == n - 1 and updated:
            return True
    return False

for _ in range(m):
    x, y, t = map(int, input().split())
    edges.append((x, y, t))

print("possible" if Bellman_Ford(n, edges) else "not possible")