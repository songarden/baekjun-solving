import sys
from collections import deque


n, m = map(int,sys.stdin.readline().split())

tomatoes = []
visited = [[False for _ in range(n)] for _ in range(m)]

for i in range(m) :
    tomatoes.append(list(map(int,sys.stdin.readline().split())))
    
def bfs_tomatoes(n , m) : 
    
    queue = deque()
    maxDay = 0
    isTomato = False
    for i in range(m):
        for j in range(n) :
            if not isTomato and tomatoes[i][j] == 0 :
                isTomato = True
            if tomatoes[i][j] == 1 :
                queue.append([i,j])
                visited[i][j] = True
    
    while(queue and isTomato) :
        a , b = queue.popleft()
        for i,j in (0,1),(1,0),(0,-1),(-1,0) :
            if 0<=a+i<m and 0<=b+j<n :
                if not visited[a+i][b+j] and tomatoes[a+i][b+j] == 0 :
                    visited[a+i][b+j] = True
                    queue.append([a+i,b+j])
                    tomatoes[a+i][b+j] = tomatoes[a][b] + 1
                    maxDay = max(maxDay,tomatoes[a+i][b+j] - 1)
    
    for i in range(m):
        for j in range(n):
            if tomatoes[i][j] == 0 :
                maxDay = -1
                break
    
    return maxDay

print(bfs_tomatoes(n,m))