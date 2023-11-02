import sys

n = int(sys.stdin.readline())
stair = []
for _ in range(n):
    stair.append(int(sys.stdin.readline()))

dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0][1] = stair[0]

if n >= 2:
    dp[1][1] = stair[0]+stair[1]
    dp[1][2] = stair[1]
    for i in range(2,n):
        dp[i][1] = dp[i-1][2] + stair[i]
        dp[i][2] = max(dp[i-2][1],dp[i-2][2]) + stair[i]

result = max(dp[n-1][1],dp[n-1][2])
print(result)