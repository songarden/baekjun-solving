import sys
import math

n = int(sys.stdin.readline())
number=[]
for i in range(n):
    number.append(int(sys.stdin.readline()))
if n == 1:
    print(number[0])
    sys.exit()
dp = [[0 for _ in range(n+1)]for _ in range(3)]

dp[0][0] = 0
dp[1][0] = 0
dp[2][0] = 0
dp[0][1] = 0
dp[1][1] = number[0]
dp[2][1] = number[0]
dp[0][2] = number[0]
dp[1][2] = number[0]+number[1]
dp[2][2] = number[1]
addSum = [0 for _ in range(n+1)]
addSum[0] = 0
addSum[1] = number[0]
addSum[2] = number[0]+number[1]
if n > 2:
    for i in range(3,n+1):
        dp[0][i] = addSum[i-1]
        dp[1][i] = addSum[i-3] + number[i-1] + number[i-2]
        dp[2][i] = addSum[i-2] + number[i-1]
        addSum[i] = max(dp[0][i],dp[1][i],dp[2][i])


print(addSum[n])