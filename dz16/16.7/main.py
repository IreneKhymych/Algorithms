import sys
sys.setrecursionlimit(1 << 25)

n, m = map(int, input().split())
parent = list(map(int, input().split()))
a1, a2 = map(int, input().split())
x, y, z = map(int, input().split())

LOG = 17
tree = [[] for _ in range(n)]
up = [[-1] * LOG for _ in range(n)]
depth = [0] * n

for i in range(1, n):
    tree[parent[i - 1]].append(i)

def Depth_First_Search(v, p):
    up[v][0] = p
    for i in range(1, LOG):
        if up[v][i - 1] != -1:
            up[v][i] = up[up[v][i - 1]][i - 1]
    for to in tree[v]:
        depth[to] = depth[v] + 1
        Depth_First_Search(to, v)

Depth_First_Search(0, -1)

def lowest(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    for i in reversed(range(LOG)):
        if up[u][i] != -1 and depth[up[u][i]] >= depth[v]:
            u = up[u][i]
    if u == v:
        return u
    for i in reversed(range(LOG)):
        if up[u][i] != -1 and up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]
    return up[u][0]

a = [0] * (2 * m + 1)
a[1], a[2] = a1, a2
ans_sum = 0
v = lowest(a[1], a[2])
ans_sum += v

for i in range(2, m + 1):
    a[2 * i - 1] = (x * a[2 * i - 3] + y * a[2 * i - 2] + z) % n
    a[2 * i] = (x * a[2 * i - 2] + y * a[2 * i - 1] + z) % n
    u = (a[2 * i - 1] + v) % n
    v = lowest(u, a[2 * i])
    ans_sum += v

print(ans_sum)