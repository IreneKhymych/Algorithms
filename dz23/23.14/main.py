import sys
sys.setrecursionlimit(10**6)

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        rev_graph[v - 1].append(u - 1)

    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    component = [-1] * n
    curr_comp = 0

    def dfs2(u):
        component[u] = curr_comp
        for v in rev_graph[u]:
            if component[v] == -1:
                dfs2(v)

    for u in reversed(order):
        if component[u] == -1:
            dfs2(u)
            curr_comp += 1

    cond_edges = set()
    for u in range(n):
        for v in graph[u]:
            if component[u] != component[v]:
                cond_edges.add((component[u], component[v]))

    print(len(cond_edges))

if __name__ == "__main__":
    main()