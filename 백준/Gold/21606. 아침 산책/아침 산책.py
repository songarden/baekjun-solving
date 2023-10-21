from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = {}

isInside = list(map(int,sys.stdin.readline().strip()))
visited = [False for _ in range(n+1)]
count = 0
while True:
    try:
        u , v = map(int,sys.stdin.readline().strip().split())
        if not u in tree:
            tree[u] = [v]
        else:
            tree[u].append(v)
        if not v in tree:
            tree[v] = [u]
        else:
            tree[v].append(u)
    except:
        break



def dfs(v):
    inside_count = 0
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            if isInside[i-1]:
                inside_count += 1
                continue
            else :
                inside_count += dfs(i)
    return inside_count

for i in tree.keys():
    if not isInside[i-1]:
        if not visited[i]:
            inside_count = dfs(i)
            count += inside_count*(inside_count-1)
    else:
        for j in tree[i]:
            if isInside[j-1]:
                count +=1  


print(count)