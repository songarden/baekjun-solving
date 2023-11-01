from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

INF = float('inf')

n , small_stone_count = map(int,sys.stdin.readline().split())
walk_stack = int(math.sqrt(2*n))

stone_log=[[INF for _ in range(walk_stack+2)] for _ in range(n+1)]
stone_log[1][0] = 0

small_stones = defaultdict(int)

for _ in range(small_stone_count):
    small_stone = int(sys.stdin.readline())
    small_stones[small_stone] = 1

for i in range(2,n+1):
    last_stone = int(math.sqrt(2*i))
    for j in range(1,last_stone+1):
        if small_stones[i] == 1:
            break
        
        stone_log[i][j] = min(stone_log[i-j][j],stone_log[i-j][j-1],stone_log[i-j][j+1]) + 1

answer = float('inf')
for i in range(walk_stack+1):
    answer = min(answer,stone_log[n][i])

if answer >= float('inf'):
    print(-1)
else:
    print(answer)