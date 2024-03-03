import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]

for i in range(n):
    t,p = map(int,sys.stdin.readline().split())
    if t+i <= n :
        dp[t+i] = max(dp[t+i],dp[i]+p)
        for j in range(t+i+1,n+1):
            dp[j] = max(dp[t+i],dp[j])

print(dp[n])