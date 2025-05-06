from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

positions = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == '@']
start = positions[0]
end = positions[1]

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2),  (1, 2),  (2, -1),  (2, 1)]

visited = [[False]*n for _ in range(n)]
parent = [[None]*n for _ in range(n)]

queue = deque()
sx, sy = start
queue.append((sx, sy))
visited[sx][sy] = True

found = False

while queue:
    x, y = queue.popleft()
    if (x, y) == end:
        found = True
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

if not found:
    print("Impossible")
else:
    x, y = end
    while (x, y) != start:
        px, py = parent[x][y]
        if (px, py) != start:
            grid[px][py] = '@'
        x, y = px, py

    for row in grid:
        print("".join(row))