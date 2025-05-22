import math
import heapq
import sys

def prim(n, coords):
    visited = [False] * n
    min = [float('inf')] * n
    min[0] = 0.0
    heap = [(0.0, 0)]
    total_cost = 0

    while heap:
        cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for v in range(n):
            if not visited[v]:
                dist = math.hypot(coords[u][0] - coords[v][0], coords[u][1] - coords[v][1])
                if dist < min[v]:
                    min[v] = dist
                    heapq.heappush(heap, (dist, v))

    return total_cost

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    coords = [(int(data[i]), int(data[i + 1])) for i in range(1, len(data), 2)]
    result = prim(n, coords)
    print(f"{result:.3f}")

