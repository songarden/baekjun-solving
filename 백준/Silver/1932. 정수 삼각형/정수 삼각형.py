from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
num_sum = []
for _ in range(n):
    num_sum.append(list(map(int,sys.stdin.readline().split())))

for i in range(n-2,-1,-1):
    for j in range(i+1):
        num_sum[i][j] += max(num_sum[i+1][j],num_sum[i+1][j+1])

print(num_sum[0][0])