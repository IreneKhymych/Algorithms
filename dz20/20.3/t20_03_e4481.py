from math import log2, ceil, gcd

class SegmentTree:
    def __init__(self, array):
        self.k = len(array)
        self.p = ceil(log2(self.k))
        self.n = 2 ** self.p
        self._items = [0] * (2 * self.n)

        for i in range(self.k):
            self._items[self.n + i] = array[i]

        for i in range(self.n - 1, 0, -1):
            self._items[i] = gcd(self._items[2 * i], self._items[2 * i + 1])

    def query(self, a, b):
        res = 0
        left = a + self.n
        right = b + self.n

        while left <= right:
            if left % 2 == 1:
                res = gcd(res, self._items[left])
                left += 1
            if right % 2 == 0:
                res = gcd(res, self._items[right])
                right -= 1
            left //= 2
            right //= 2

        return res

    def update(self, i, value):
        i += self.n
        self._items[i] = value
        i //= 2
        while i > 0:
            self._items[i] = gcd(self._items[2 * i], self._items[2 * i + 1])
            i //= 2

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

gcd_tree = SegmentTree(arr)

for q in queries:
    if q[0] == 1:
        _, l, r = q
        print(gcd_tree.query(l - 1, r - 1))
    else:
        _, i, val = q
        gcd_tree.update(i - 1, val)
