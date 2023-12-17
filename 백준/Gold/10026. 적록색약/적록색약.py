import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())

rgbMap = []
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    rgbMap.append(list(map(str,sys.stdin.readline().strip())))

def dfs(isBlind,i,j) :
    global n
    color = rgbMap[i][j]
    visited[i][j] = True
    for di,dj in (0,1),(1,0),(0,-1),(-1,0):
        if n>di+i>=0 and n>dj+j>=0:
            if not visited[di+i][dj+j]:
                if (color == 'R' or color == 'G') and isBlind:
                    if not rgbMap[i+di][j+dj] == 'B':
                        dfs(isBlind,i+di,j+dj)
                else:
                    if rgbMap[i+di][j+dj] == color:
                        dfs(isBlind,i+di,j+dj)
ans = [0,0]            
for k in range(2):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(k,i,j)
                ans[k] = ans[k] + 1

print(ans[0],ans[1])