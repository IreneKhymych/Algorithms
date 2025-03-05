import sys

def sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def main():
    n = int(sys.stdin.readline().strip())
    robots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    sorted_robots = sort(robots)
    for p, a in sorted_robots:
        print(p, a)

if __name__ == "__main__":
    main()

