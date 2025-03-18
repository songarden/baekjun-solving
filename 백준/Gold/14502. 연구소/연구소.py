import sys

n,m = map(int,sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]* m for _ in range(n)]
origin_safe = -3
temp_save = 0
result = 0

def run(i,j):
    global temp_save
    global visited
    if temp_save == 0:
        return
    for x,y in (0,1),(1,0),(0,-1),(-1,0) :
        if 0<=i+x<n and 0<=j+y<m :
            if grid[i+x][j+y] == 0 and not visited[i+x][j+y]:
                temp_save = temp_save - 1
                visited[i+x][j+y] = 1
                run(i+x,j+y)

def walling(q,w,e,r,t,y):
    grid[q][w] = 1
    grid[e][r] = 1
    grid[t][y] = 1
    global temp_save
    global visited
    global result
    temp_save = origin_safe
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                visited[i][j] = 1
                run(i,j)
    if temp_save > result :
        result = temp_save
    visited = [[0]* m for _ in range(n)]
    grid[q][w] = 0
    grid[e][r] = 0
    grid[t][y] = 0

safe_zone = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            safe_zone.append((i,j))
            origin_safe = origin_safe + 1
            
if origin_safe > 0 :
    for i in range(len(safe_zone)):
        for j in range(i+1,len(safe_zone)):
            for k in range(j+1,len(safe_zone)):
                a,b = safe_zone[i]
                c,d = safe_zone[j]
                e,f = safe_zone[k]
                walling(a,b,c,d,e,f)
    print(result)
else :
    print(0)
            

                    
                    
                        