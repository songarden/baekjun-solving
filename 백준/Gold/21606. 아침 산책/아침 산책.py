from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
tree = {}

isInside = list(map(int,sys.stdin.readline().strip()))
visited = [False for _ in range(n+1)]
count = 0
for i in range(n-1):
    u , v = map(int,sys.stdin.readline().strip().split())
    if not u in tree:
        tree[u] = [v]
    else:
        tree[u].append(v)
    if not v in tree:
        tree[v] = [u]
    else:
        tree[v].append(u)



def dfs_walk(v):
    global count
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            if isInside[i-1]:
                count += 1
                continue
            else :
                dfs_walk(i)

for i in tree.keys():
    if isInside[i-1]:
        dfs_walk(i)
        visited = [False for _ in range(n+1)]

print(count)