from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
list_map = []
for _ in range(n):
    list_map.append(list(map(int,sys.stdin.readline().split())))


for k in range(n):
    for i in range(n):
        for j in range(n):
            if list_map[i][k] == 1 and list_map[k][j]:
                list_map[i][j] = 1

for i in range(n):
    print(*list_map[i])