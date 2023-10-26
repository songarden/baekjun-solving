from collections import deque
import copy
import heapq
import sys


n,k = map(int,sys.stdin.readline().strip().split())
virusMap = []

for _ in range(n):
    virusMap.append(list(map(int,sys.stdin.readline().strip().split())))

visited = [[False for _ in range(n)] for _ in range(n)]



def bfs(time):
    global n
    global k
    this_time = time
    temp_heap = []
    heap = []
    heapq.heapify(heap)
    for i in range(n):
        for j in range(n):
            if virusMap[i][j] != 0 and not visited[i][j]:
                heapq.heappush(heap,(virusMap[i][j],i,j))
                visited[i][j] = True

    while this_time > 0:
        virus,x,y = heapq.heappop(heap)
        for i,j in (0,1),(1,0),(0,-1),(-1,0):
            if n>x+i>=0 and n>y+j>=0:
                if virusMap[x+i][y+j] == 0 and not visited[x+i][y+j]:
                    virusMap[x+i][y+j] = virus
                    temp_heap.append((virus,x+i,y+j))
                    visited[x+i][y+j] = True
                    
        if not heap:
            if not temp_heap:
                break
            else:
                heap = copy.deepcopy(temp_heap)
                temp_heap.clear()
                this_time -= 1

s,x,y = map(int,sys.stdin.readline().strip().split())
bfs(s)
print(virusMap[x-1][y-1])