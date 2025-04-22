n, m = map(int, input().split())
degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    degree[a] += 1
    degree[b] += 1

for i in range(1, n + 1):
    print(degree[i])
