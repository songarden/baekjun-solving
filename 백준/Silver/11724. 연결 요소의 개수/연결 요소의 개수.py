from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**8)

n , m = map(int,sys.stdin.readline().strip().split())
count = 0
isVisited = False
graph={}
for _ in range(m):
    v1 , v2 = map(int,sys.stdin.readline().strip().split())
    if not v1 in graph:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)
    if not v2 in graph:
        graph[v2] = [v1]
    else:
        graph[v2].append(v1)
    
visited = [False for _ in range(n+1)]

def dfs(start):
    global isVisited
    if visited[start] == True:
        return
    visited[start] = True
    isVisited = True
    if start in graph:
        for i in graph[start]:
            if not visited[i]:
                dfs(i)

for i in range(n):
    dfs(i+1)
    if isVisited:
        count +=1
    isVisited = False

print(count)