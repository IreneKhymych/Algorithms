def bubble(arr):
    n = len(arr)
    cnt = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
    return cnt

n = int(input())
arr = list(map(int, input().split()))
print(bubble(arr))
