n, m = map(int, input().split())
In = [0] * (n + 1)
out = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    out[a] += 1
    In[b] += 1

for i in range(1, n + 1):
    print(In[i], out[i])
