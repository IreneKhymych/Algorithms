n, m = map(int, input().split())
edges = set()

multiedge = False

for _ in range(m):
    a, b = map(int, input().split())
    if (a, b) in edges:
        multiedge = True
        break
    edges.add((a, b))

if multiedge:
    print("YES")
else:
    print("NO")
