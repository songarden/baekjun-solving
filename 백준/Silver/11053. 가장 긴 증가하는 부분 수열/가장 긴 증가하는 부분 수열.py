from collections import deque
import heapq
import re
import sys
sys.setrecursionlimit(10**8)


n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().strip().split()))

dp = [0 for _ in range(n)]
result = 0
for i in range(n):
    max_dp = 0
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        else:
            max_dp = max(max_dp,dp[j])
    dp[i] = max_dp+1
    result = max(result,dp[i])

print(result)