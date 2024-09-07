n, x = map(int, input().split())
a = list(map(int, input().split()))

def cal():
    dp = [float('inf')] * (x + 1)
    dp[0] = 0
    for i in t:
        for j in range(x, i - 1, -1):
            dp[j] = min(dp[j], dp[j - i] + 1)
    return dp[x]

t = [i // 2 for i in a]
res = cal()

for i in range(n):
    t[i] = a[i]
    res = min(res, cal())
    t[i] //= 2

print(res if res != float('inf') else -1)
