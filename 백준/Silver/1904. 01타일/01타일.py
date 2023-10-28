from collections import deque
import heapq
import re
import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
result = [1,2] #+ [0 for _ in range (n-2)]

for i in range(2,n):
    result.append((result[i-1]+result[i-2])%15746)

print(result[n-1]%15746)