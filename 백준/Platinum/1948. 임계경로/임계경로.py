from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
world = {}
back_world = {}
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    v1, v2, time = map(int,sys.stdin.readline().strip().split())
    if not v1 in world:
        world[v1] = [(v2,time)]
    else :
        world[v1].append((v2,time))
    if not v2 in back_world:
        back_world[v2] = [(v1,time)]
    else:
        back_world[v2].append((v1,time))
    indegree[v2] += 1

start , end = map(int,sys.stdin.readline().strip().split())

memorize = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
queue = deque()
def bfs():
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now in world:
            for next,cost in world[now]:
                memorize[next] = max(memorize[next],cost+memorize[now])
                indegree[next] -=1
                if indegree[next] == 0:
                    queue.append(next)




def back_bfs():
    queue.append(end)
    count = 0
    while queue:
        now = queue.popleft()
        if not now in back_world:
            continue
        visited[now] = True
        for pre,cost in back_world[now]:
                if memorize[now] == memorize[pre]+cost:
                    count +=1
                    if not visited[pre]:
                        queue.append(pre)
                        visited[pre] = True
    print(count)
                
if n ==1 and m==1:
    print(world[start][1])
    print(1)
else:
    bfs()
    print(memorize[end])
    back_bfs()