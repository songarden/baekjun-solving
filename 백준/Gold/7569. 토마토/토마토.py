from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

tomato = []

m,n,h = map(int,sys.stdin.readline().strip().split())
tomato= [[list(map(int,sys.stdin.readline().strip().split()))for _ in range(n)]for _ in range(h)]
visited = [[[False for _ in range(m)]for _ in range(n)]for _ in range(h)]



def bfs():
    global m
    global n
    global h
    queue = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 1:
                    queue.append([k,i,j])
                    visited[k][i][j] = True
    while queue:
        thisK , thisI, thisJ = queue.popleft()
        for k,i,j in (0,0,1),(0,1,0),(0,0,-1),(0,-1,0),(1,0,0),(-1,0,0):
            if thisK+k > h-1 or thisK+k < 0 or thisI+i > n-1 or thisI+i <0 or thisJ+j >m-1 or thisJ+j <0:
                continue
            else:
                if not visited[thisK+k][thisI+i][thisJ+j] and not tomato[thisK+k][thisI+i][thisJ+j] < 0:
                    tomato[thisK+k][thisI+i][thisJ+j] = tomato[thisK][thisI][thisJ]+1
                    visited[thisK+k][thisI+i][thisJ+j] = True
                    queue.append([thisK+k,thisI+i,thisJ+j])
def day_count_def():
    day_count =0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0:
                    day_count = -1
                    return day_count
                if tomato[k][i][j] > day_count:
                    day_count = tomato[k][i][j]
    return day_count-1

                

bfs()
print(day_count_def())