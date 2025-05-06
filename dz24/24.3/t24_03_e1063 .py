from collections import deque

m, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
components = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] == '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for i in range(m):
    for j in range(n):
        if grid[i][j] == '#' and not visited[i][j]:
            bfs(i, j)
            components += 1

print(components)
