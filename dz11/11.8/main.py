import sys
with open('input.txt', 'r') as f:
    lines = f.readlines()

n, t = map(int, lines[0].split())
arr = list(map(int, lines[1].split()))

def count(arr, t):
    def merge(arr, temp_arr, left, mid, right, t):
        i, j, k = left, mid + 1, left
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] > arr[j] + t:
                inv_count += (mid - i + 1)
                j += 1
            else:
                i += 1
        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    def merge_and_count(arr, temp_arr, left, right, t):
        if left >= right:
            return 0
        mid = (left + right) // 2
        inv_count = merge_and_count(arr, temp_arr, left, mid, t)
        inv_count += merge_and_count(arr, temp_arr, mid + 1, right, t)
        inv_count += merge(arr, temp_arr, left, mid, right, t)
        return inv_count

    n = len(arr)
    temp_arr = [0] * n
    return merge_and_count(arr, temp_arr, 0, n - 1, t)

with open('output.txt', 'w') as f:
    f.write(str(count(arr, t)))