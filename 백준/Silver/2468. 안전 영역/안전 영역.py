from collections import deque
import sys

n = int(sys.stdin.readline())

city = []
visited = [[False for _ in range(n)] for _ in range(n)]
min_height = 101
max_height = 0
max_count = 1
count = 0

def visited_reset():
    global n
    global visited
    visited = [[False for _ in range(n)] for _ in range(n)]


# print(min_height)
# print(max_height)

#city input
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    if min_height > min(line):
        min_height = min(line)
    if max_height < max(line):
        max_height = max(line)
    city.append(line)

# print(min_height)
# print(max_height)
def water_fall(x):
    global n
    for i in range(n):
        for j in range(n):
            city[i][j] -=x

# print(city)
# print(max_height)

#서북동남 순
#DFS
# def dfs(i,j):
#     visited[i][j] = True
#     if not j == 0 and not visited[i][j-1] and not city[i][j-1] <= 0:
#         dfs(i,j-1)
#     if not i == 0 and not visited[i-1][j] and not city[i-1][j] <= 0:
#         dfs(i-1,j)
#     if not j == n-1 and not visited[i][j+1] and not city[i][j+1] <= 0:
#         dfs(i,j+1)
#     if not i == n-1 and not visited[i+1][j] and not city[i+1][j] <= 0:
#         dfs(i+1,j)

def bfs(i,j):
    visited[i][j] = True
    queue = deque()
    if not j == 0 and not visited[i][j-1] and not city[i][j-1] <= 0:
        queue.append([i,j-1])
    if not i == 0 and not visited[i-1][j] and not city[i-1][j] <= 0:
        queue.append([i-1,j])
    if not j == n-1 and not visited[i][j+1] and not city[i][j+1] <= 0:
        queue.append([i,j+1])
    if not i == n-1 and not visited[i+1][j] and not city[i+1][j] <= 0:
        queue.append([i+1,j])
    while queue:
        travel_command = queue.popleft()
        x = travel_command[0]
        y = travel_command[1]
        visited[x][y] = True
        if not y == 0 and not visited[x][y-1] and not city[x][y-1] <= 0:
            visited[x][y-1] = True
            queue.append([x,y-1])
        if not x == 0 and not visited[x-1][y] and not city[x-1][y] <= 0:
            visited[x-1][y] = True
            queue.append([x-1,y])
        if not y == n-1 and not visited[x][y+1] and not city[x][y+1] <= 0:
            visited[x][y+1] = True
            queue.append([x,y+1])
        if not x == n-1 and not visited[x+1][y] and not city[x+1][y] <= 0:
            visited[x+1][y] = True
            queue.append([x+1,y])
        


water_fall(min_height-1)
for k in range(max_height-min_height):
    water_fall(1)
    visited_reset()
    for i in range(n):
        for j in range(n):
            if not city[i][j]<=0 and not visited[i][j]:
                bfs(i,j)
                count +=1
    if max_count < count:
        max_count = count
    count = 0


print(max_count)