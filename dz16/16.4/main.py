class Official:
    def __init__(self, bribe):
        self.bribe = bribe
        self.subordinates = []

    def add(self, subordinate):
        self.subordinates.append(subordinate)

    def min(self):
        if not self.subordinates:
            return self.bribe
        return self.bribe + min(sub.min() for sub in self.subordinates)

def tree(data):
    officials = {i + 1: Official(data[i][0]) for i in range(len(data))}

    for i, (_, count, *subs) in enumerate(data):
        for sub in subs:
            officials[i + 1].add(officials[sub])

    return officials[1]

def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    minister = tree(data)
    print(minister.min())

if __name__ == "__main__":
    main()