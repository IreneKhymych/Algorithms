MOD = 301907
s = input().strip()

def sequences(s):
    n = len(s)
    stack = []
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n):
        next = [0] * (n + 1)
        for j in range(n + 1):
            if dp[j] == 0:
                continue
            if s[i] in "(?":
                next[j + 1] = (next[j + 1] + dp[j]) % MOD
            if s[i] in ")?":
                if j > 0:
                    next[j - 1] = (next[j - 1] + dp[j]) % MOD
        dp = next

    return dp[0]

print(sequences(s))