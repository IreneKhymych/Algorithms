from collections import deque

def operations(s):
    results = []

    if s[0] != '9':
        results.append(str(int(s[0]) + 1) + s[1:])

    if s[-1] != '1':
        results.append(s[:-1] + str(int(s[-1]) - 1))

    results.append(s[-1] + s[:-1])
    results.append(s[1:] + s[0])

    return [r for r in results if '0' not in r]

def bfs(start, end):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path

        for neighbor in operations(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []

start = input().strip()
end = input().strip()

path = bfs(start, end)
for number in path:
    print(number)