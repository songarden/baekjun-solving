import sys
from collections import deque
sys.setrecursionlimit(10**8)

n , m = map(int,sys.stdin.readline().split())
mapList = []
for _ in range(n):
    mapList.append(list(map(int,sys.stdin.readline().strip())))

visited = [[[False for _ in range(2)] for _ in range(m)]for _ in range(n)]

def bfs(i,j):
    global n,m
    queue = deque()
    count = 1
    queue.append((i,j,1,count))
    while queue:
        i,j,punch,count = queue.popleft()
        if mapList[i][j] == 1:
            punch = 0
        if i == n-1 and j == m-1:
            return count
        for di,dj in (0,1), (1,0) , (0,-1) , (-1,0):
            if n-1>=i+di>=0 and m-1>=j+dj>=0:
                
                if mapList[i+di][j+dj] == 1 and punch == 1:
                    if not visited[i+di][j+dj][0]:
                        queue.append((i+di,j+dj,0,count+1))
                        visited[i+di][j+dj][0] == True
                elif mapList[i+di][j+dj] == 1 and punch == 0:
                    continue
                else:
                    if not visited[i+di][j+dj][punch]:
                        queue.append((i+di,j+dj,punch,count+1))
                        visited[i+di][j+dj][punch] = True
    return -1
                        
print(bfs(0,0))