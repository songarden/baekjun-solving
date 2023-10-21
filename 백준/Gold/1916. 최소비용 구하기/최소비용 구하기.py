from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

# test = [1,2]
# a,b = test
# print(a)
# print(b)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
city = {}
visited = [False for _ in range(n+1)]

for _ in range(m):
    v1,v2,cost = map(int,sys.stdin.readline().strip().split())
    if not v1 in city:
        city[v1] = [[cost,v2]]
    else :
        city[v1].append([cost,v2])

start , end = map(int,sys.stdin.readline().strip().split())

def dijkstra(start):
    global end
    costMin = [float('inf')]*(n+1)
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap,[0,start])
    costMin[start] = 0
    while heap:
        cost , vertex = heapq.heappop(heap)
        visited[vertex] = True
        if vertex == end:
            return cost
        if vertex in city:
            for i,j in city[vertex]:
                if not visited[j] and costMin[j] > cost + i:
                    heapq.heappush(heap,[cost+i,j])
                    costMin[j] = cost+i
        

print(dijkstra(start))