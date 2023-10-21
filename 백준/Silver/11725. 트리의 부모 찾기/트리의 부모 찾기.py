from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())

parent = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

tree = {}

for _ in range(n-1):
    v1 , v2 = map(int,sys.stdin.readline().strip().split())
    if not v1 in tree:
        tree[v1] = [v2]
    else:
        tree[v1].append(v2)
    if not v2 in tree:
        tree[v2] = [v1]
    else:
        tree[v2].append(v1)

def bfs(start):
    before = 0
    queue = deque()
    queue.append(start)
    while queue:
        thisV = queue.popleft()
        visited[thisV] = True
        if thisV in tree:
            for i in tree[thisV]:
                if not visited[i]:
                    parent[i] = thisV
                    queue.append(i)

bfs(1)
for i in range(2,n+1):
    print(parent[i])