import sys
input = sys.stdin.readline

MOD1 = 12345
MOD2 = 23456
MAX_N = 100005

k = int(input())
queries = []
max_index = 0

def a_n(n):
    return (n * n % MOD1) + (n * n * n % MOD2)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.min_tree = [0] * (4 * self.n)
        self.max_tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, data)

    def build(self, node, l, r, data):
        if l == r:
            self.min_tree[node] = data[l]
            self.max_tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self.build(2 * node, l, mid, data)
            self.build(2 * node + 1, mid + 1, r, data)
            self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])
            self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])

    def update(self, node, l, r, idx, val):
        if l == r:
            self.min_tree[node] = val
            self.max_tree[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node, l, mid, idx, val)
            else:
                self.update(2 * node + 1, mid + 1, r, idx, val)
            self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])
            self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return float('inf'), float('-inf')
        if ql <= l and r <= qr:
            return self.min_tree[node], self.max_tree[node]
        mid = (l + r) // 2
        left_min, left_max = self.query(2 * node, l, mid, ql, qr)
        right_min, right_max = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return min(left_min, right_min), max(left_max, right_max)

for _ in range(k):
    x, y = map(int, input().split())
    queries.append((x, y))
    if x > 0:
        max_index = max(max_index, y)
    else:
        max_index = max(max_index, -x)

arr = [a_n(i + 1) for i in range(max_index)]
seg_tree = SegmentTree(arr)

for x, y in queries:
    if x > 0:
        l = x - 1
        r = y - 1
        mn, mx = seg_tree.query(1, 0, max_index - 1, l, r)
        print(mx - mn)
    else:
        idx = -x - 1
        seg_tree.update(1, 0, max_index - 1, idx, y)
