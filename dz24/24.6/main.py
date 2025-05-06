import sys
sys.setrecursionlimit(10000)

N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]
max_lake = 0

for _ in range(K):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def valid(x, y):
    return 0 <= x < N and 0 <= y < M and grid[x][y] == 1

def dfs(x, y):
    grid[x][y] = -1
    size = 1
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if valid(nx, ny):
            size += dfs(nx, ny)
    return size


for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            max_lake = max(max_lake, dfs(i, j))

print(max_lake)