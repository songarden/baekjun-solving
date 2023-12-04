import sys
sys.setrecursionlimit(10**8)

r,c = map(int,sys.stdin.readline().split())

bread_map = []
visited = [[False for _ in range(c)]for _ in range(r)]
for _ in range(r):
    bread_map.append(list(map(str,sys.stdin.readline().strip())))
    

def dfs(i,j):
    global r,c
    visited[i][j] = True
    if j == c-1:
        return 1
    ans = 0
    for di,dj in (-1,1),(0,1),(1,1):
        if not r-1>=i+di>=0 or not c-1>=j+dj>=0:
            continue
        if not bread_map[i+di][j+dj] == 'x' and not visited[i+di][j+dj]:
            ans = dfs(i+di,j+dj)
            if ans == 1:
                return 1
    
    if ans == 0:
        visited[i][j] == False
        return 0
ans = 0
for i in range(0,r):
    ans += dfs(i,0)

print(ans)