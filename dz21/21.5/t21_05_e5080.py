n = int(input())
count = 0

for _ in range(n):
    m = list(map(int, input().split()))
    if sum(m) == 1:
        count += 1

print(count)
