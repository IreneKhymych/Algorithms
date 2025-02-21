class HashSet:
    EMPTY = []

    def __init__(self, size=100003):
        self.size = size
        self.table = [self.EMPTY[:] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def contains(self, key):
        index = self._hash(key)
        return key in self.table[index]


n = int(input())
numbers = list(map(int, input().split()))
hash_set = HashSet()

for num in numbers:
    hash_set.insert(num)

print(sum(len(bucket) for bucket in hash_set.table))
