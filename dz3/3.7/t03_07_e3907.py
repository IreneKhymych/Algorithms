from collections import Counter
n = int(input())
colors = list(map(int, input().split()))
m = int(input())
animals = list(map(int, input().split()))
color_count = Counter(colors)
for animal in animals:
    print(color_count.get(animal, 0))
