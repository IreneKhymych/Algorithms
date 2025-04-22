n, m = map(int, input().split())
edge = set()

for _ in range(m):
    a, b = map(int, input().split())
    edge.add(tuple(sorted((a, b))))

expected_edges = n * (n - 1) // 2

if len(edge) == expected_edges:
    print("YES")
else:
    print("NO")
