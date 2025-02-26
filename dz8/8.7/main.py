n = int(input())
arr = list(map(int, input().split()))

def sort(arr):
    n = len(arr)
    flag = True
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if j + 1 != i:
            print(" ".join(map(str, arr)))
            flag = False
    if flag:
        return

sort(arr)
