n = int(input())
arr = [input().strip() for _ in range(n)]

def sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr

sorted = sort(arr)
print("\n".join(sorted))
