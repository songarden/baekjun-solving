from collections import deque,defaultdict
import heapq
import re
import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
graph = [[0 for _ in range(n+1)]]
for _ in range(n):
    graph.append([0]+list(map(int,sys.stdin.readline().split())))
dp = defaultdict(lambda: float('inf'))

def dfs(this,visit):
    global n
    if visit == (1<<n) - 1:
        if graph[this][1] == 0:
            return float('inf')
        else:
            return graph[this][1]
    
    if (this,visit) in dp:
        return dp[(this,visit)]
    
    for i in range(1,n+1):
        if not visit & 1<<(i-1) and not graph[this][i] == 0:
            weight = dfs(i,visit|1<<(i-1))+graph[this][i]
            dp[(this,visit)] = min(dp[(this,visit)],weight)
    return dp[(this,visit)]


print(dfs(1,1))