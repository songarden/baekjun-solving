from collections import deque
import copy
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = {} # { 자식 : [부모1, ...] }
matrix = []
outdegree = [0 for _ in range(n+1)]
result = [0 for i in range(n)]
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().strip())))
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            if not j+1 in graph:
                graph[j+1] = [i+1]
            else:
                graph[j+1].append(i+1)
            outdegree[i+1] += 1



def bfs_change(n):
    heap =[]
    heapq.heapify(heap)
    for i in range(1,n+1):
        if outdegree[i] == 0:
            heapq.heappush(heap,i*(-1))
    if not heap:
        result[0] = 0
        return
    for x in range(n,0,-1):
        now = (heapq.heappop(heap))*(-1)
        if now in graph:
            for son in graph[now]:
                outdegree[son] -= 1
                if outdegree[son] == 0:
                    heapq.heappush(heap,son*(-1))
        result[now-1] = x

bfs_change(n)
if result[0] == 0:
    print(-1)
else:
    print(' '.join(list(map(str,result))))