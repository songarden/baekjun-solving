from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

INF = float('inf')

v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
g = {}
result = [INF for _ in range(v)]
result[start-1] = 0
for i in range(e):
    x,y,cost = map(int,sys.stdin.readline().split())
    if x == start:
        result[y-1] = min(result[y-1],cost)
    if not x in g:
        g[x] = [(y,cost)]
    else:
        g[x].append((y,cost))

heap = []
heapq.heapify(heap)
visited = [False for _ in range(v)]
visited[start-1] = True
for info in g[start]:
    node , c = info
    heapq.heappush(heap,(c,node))

while heap :
    thisCost , this = heapq.heappop(heap)
    if visited[this-1]:
        continue
    visited[this-1] = True
    if not this in g:
        continue
    else:
        for info in g[this]:
            n,nextCost = info
            if not visited[n-1]:
                if result[n-1] > thisCost+nextCost:
                    result[n-1] = thisCost+nextCost
                    heapq.heappush(heap,(result[n-1],n))


for ans in result:
    if ans == INF:
        print('INF')
    else:
        print(ans)