import sys
import math

input = sys.stdin.read

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

class SegmentTree:
    def __init__(self, data, func, neutral):
        self.n = len(data)
        self.func = func
        self.neutral = neutral
        self.tree = [neutral] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = data[tl]
        else:
            tm = (tl + tr) // 2
            self._build(data, v*2+1, tl, tm)
            self._build(data, v*2+2, tm+1, tr)
            self.tree[v] = self.func(self.tree[v*2+1], self.tree[v*2+2])

    def update(self, pos, new_val, v=0, tl=0, tr=None):
        if tr is None:
            tr = self.n - 1
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(pos, new_val, v*2+1, tl, tm)
            else:
                self.update(pos, new_val, v*2+2, tm+1, tr)
            self.tree[v] = self.func(self.tree[v*2+1], self.tree[v*2+2])

    def query(self, l, r, v=0, tl=0, tr=None):
        if tr is None:
            tr = self.n - 1
        if l > r:
            return self.neutral
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left = self.query(l, min(r, tm), v*2+1, tl, tm)
        right = self.query(max(l, tm+1), r, v*2+2, tm+1, tr)
        return self.func(left, right)

def main():
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1
    arr = list(map(int, data[idx:idx+n]))
    idx += n

    gcd_tree = SegmentTree(arr, math.gcd, 0)
    lcm_tree = SegmentTree(arr, lcm, 1)

    m = int(data[idx])
    idx += 1

    result = []
    for _ in range(m):
        q = int(data[idx])
        l = int(data[idx+1]) - 1
        r = int(data[idx+2])
        idx += 3

        if q == 1:
            r -= 1
            gcd_val = gcd_tree.query(l, r)
            lcm_val = lcm_tree.query(l, r)
            if gcd_val < lcm_val:
                result.append("wins")
            elif gcd_val > lcm_val:
                result.append("loser")
            else:
                result.append("draw")
        else:
            gcd_tree.update(l, r)
            lcm_tree.update(l, r)

    print('\n'.join(result))

if __name__ == "__main__":
    main()