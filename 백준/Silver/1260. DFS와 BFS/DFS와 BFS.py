from collections import deque
import sys
import heapq

n , m , start = map(int,sys.stdin.readline().strip().split())

graph = {}
dfs_ans = []
bfs_ans = []
for _ in range(m):
    index , vertex = map(int,sys.stdin.readline().strip().split())
    if not index in graph:
        graph[index] = [vertex]
    else:
        graph[index].append(vertex)
    
    if not vertex in graph:
        graph[vertex] = [index]
    else:
        graph[vertex].append(index)
for key,value in graph.items():
    value = sorted(value)
    graph[key] = value
visited = [False for i in range(n+1)]
def dfs(v):
    visited[v] = True
    dfs_ans.append(v)
    if not v in graph:
        return
    for vertex in graph[v]:
        if not visited[vertex]:
            dfs(vertex)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        vertex = queue.popleft()
        bfs_ans.append(vertex)
        if vertex in graph:
            for i in graph[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        

dfs(start)
visited = [False for i in range(n+1)]
bfs(start)

print(' '.join(map(str,dfs_ans)))
print(' '.join(map(str,bfs_ans)))