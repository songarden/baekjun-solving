from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
count = 0
dp = [0 for _ in range(n+1)]
dp[1] = 0
for i in range(2,n+1):
    if i%3 == 0:
        if i%2 == 0:
            dp[i] = min(dp[i//3],dp[i//2],dp[i-1])+1
        else:
            dp[i] = min(dp[i//3],dp[i-1])+1
    elif i%2 == 0:
        dp[i] = min(dp[i//2],dp[i-1])+1
    else:
        dp[i] = dp[i-1] +1

print(dp[n])