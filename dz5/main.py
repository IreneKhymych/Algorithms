def max_rope_length(n, k, lengths):
    def cut(mid):
        count = 0
        for length in lengths:
            count += length // mid
        return count >= k

    left, right = 1, max(lengths)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if cut(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

n, k = map(int, input().split())
lengths = [int(input()) for _ in range(n)]
print(max_rope_length(n, k, lengths))
