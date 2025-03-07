def solve(n: int, k: int):
    def _solve(current: list[int], used: set[int]):
        if len(current) == k:
            print(" ".join(map(str, current)))
            return

        for i in range(1, n + 1):
            if i not in used:
                nums = current + [i]
                new_used = used | {i}
                _solve(nums, new_used)

    _solve([], set())

if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k)
