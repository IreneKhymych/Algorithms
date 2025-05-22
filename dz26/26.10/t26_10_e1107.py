import heapq
from collections import defaultdict

def prim(n, adj, skip_edge=None):
    visited = [False] * (n + 1)
    min_heap = []
    visited[1] = True
    for to, cost, idx in adj[1]:
        if idx != skip_edge:
            heapq.heappush(min_heap, (cost, 1, to, idx))

    total_cost = 0
    used_edges = []

    while min_heap and len(used_edges) < n - 1:
        cost, frm, to, idx = heapq.heappop(min_heap)
        if visited[to]:
            continue
        visited[to] = True
        total_cost += cost
        used_edges.append((frm, to, cost, idx))
        for neighbor, w, eid in adj[to]:
            if not visited[neighbor] and eid != skip_edge:
                heapq.heappush(min_heap, (w, to, neighbor, eid))

    if len(used_edges) == n - 1:
        return total_cost, used_edges
    else:
        return float('inf'), []

def find(n, m, edge_list):
    adj = defaultdict(list)
    for idx, (u, v, w) in enumerate(edge_list):
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))

    best_cost, mst_edges = prim(n, adj)
    second_best = float('inf')
    used_indices = {idx for _, _, _, idx in mst_edges}

    for _, _, _, idx in mst_edges:
        cost, _ = prim(n, adj, skip_edge=idx)
        if cost != float('inf') and cost >= best_cost:
            second_best = min(second_best, cost)

    if second_best == float('inf'):
        second_best = best_cost

    return best_cost, second_best

def main():
    n, m = map(int, input().split())
    edge_list = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge_list.append((a, b, c))

    s1, s2 = find(n, m, edge_list)
    print(f"{s1} {s2}")

if __name__ == "__main__":
    main()
