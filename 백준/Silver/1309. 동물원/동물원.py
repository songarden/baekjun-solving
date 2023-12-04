import sys


n=int(sys.stdin.readline())
dp = [0 for _ in range(100001)]

dp[1] = 3
dp[2] = 7

for i in range(3,n+1):
    dp[i] = (2*dp[i-1] + dp[i-2] )% 9901

print(dp[n])