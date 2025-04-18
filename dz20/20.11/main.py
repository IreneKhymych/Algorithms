class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.t = [float('-inf')] * (2 * self.size)
        for i in range(self.n):
            self.t[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.t[i] = max(self.t[i << 1], self.t[i << 1 | 1])

    def get_max(self, l, r):
        l += self.size
        r += self.size
        res = float('-inf')
        while l <= r:
            if l % 2 == 1:
                res = max(res, self.t[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.t[r])
                r -= 1
            l //= 2
            r //= 2
        return res

def max_k(arr, k):
    n = len(arr)
    seg_tree = SegmentTree(arr)
    count = 0
    r1 = r2 = 0

    for l in range(n):
        while r1 < n and seg_tree.get_max(l, r1) < k:
            r1 += 1
        if r1 == n or seg_tree.get_max(l, r1) > k:
            continue
        r2 = max(r2, r1)
        while r2 + 1 < n and seg_tree.get_max(l, r2 + 1) == k:
            r2 += 1
        count += (r2 - r1 + 1)
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2 + n]))

    print(max_k(arr, k))

if __name__ == "__main__":
    main()