import sys

n = int(sys.stdin.readline())
homes = []
for _ in range(n):
    homes.append(list(map(int,sys.stdin.readline().strip())))

visited = [[False for _ in range(n)] for _ in range(n)]
count = 0
def dfs(x,y):
    global count
    visited[x][y] = True
    count += 1
    for i,j in (0,1),(1,0),(0,-1),(-1,0):
        if n>x+i>=0 and n>y+j>=0:
            if homes[x+i][y+j] == 1 and not visited[x+i][y+j]:
                dfs(x+i,y+j)

eachHome = []       


for i in range(n):
    for j in range(n):
        if not visited[i][j] and homes[i][j] == 1:
            dfs(i,j)
            eachHome.append(count)
            count = 0
eachHome = sorted(eachHome)
print(len(eachHome))

for i in range(len(eachHome)):
    print(eachHome[i])