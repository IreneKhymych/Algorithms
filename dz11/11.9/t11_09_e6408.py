n, t = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

def count(arr, t):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j] + t:
                inv_count += 1
    return inv_count

print(count(arr, t))
