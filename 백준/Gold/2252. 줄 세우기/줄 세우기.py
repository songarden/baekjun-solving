from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

n ,m = map(int,sys.stdin.readline().strip().split())
kids = {}
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    kid1 , kid2 = map(int,sys.stdin.readline().strip().split())
    if not kid1 in kids:
        kids[kid1] = [kid2]
    else:
        kids[kid1].append(kid2)
    indegree[kid2] +=1

result = []

def kids_height_bfs():
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            if i in kids:
                queue.append(i)
            result.append(i)
    while queue:
        now = queue.popleft()
        for next in kids[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                if next in kids:
                    queue.append(next)
                result.append(next)
kids_height_bfs()
print(' '.join(list(map(str, result))))