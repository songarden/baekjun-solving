import sys

n = int(sys.stdin.readline())

boxes = list(map(int,sys.stdin.readline().split()))

dp = [1]

for i in range(1,n):
    temp = 1
    for j in range(i):
        if boxes[i] > boxes[j]:
            temp = max(temp,dp[j]+1)
    dp.append(temp)

print(max(dp))