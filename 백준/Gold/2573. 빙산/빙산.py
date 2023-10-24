from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().strip().split())
ice_world = []
for _ in range(n):
    ice_world.append(list(map(int,sys.stdin.readline().strip().split())))

def ice_to_water(): #이번 년도에 막 바다가 된 것과 이미 바다여서 면을 카운트해주는 공간을 구분해주기 위해 0과 -1로 구분
    for i in range(n):
        for j in range(m):
            if ice_world[i][j] == 0:
                ice_world[i][j] = -1

visited = [[False for _ in range(m)]for _ in range(n)]

# def watering_cal(x,y):
#     global n
#     global m
#     count = 0
#     for i,j in (0,1),(1,0),(0,-1),(-1,0):
#         if n>x+i>=0 and m>y+j>=0:
#             if ice_world[x+i][y+j] <0:
#                 count += 1
#     ice_world[x][y] -= count
#     if ice_world[x][y] < 0:
#         ice_world[x][y] = 0
watering = []

def bfs(x,y):
    global n
    global m
    queue  = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        count = 0
        now_x,now_y = queue.popleft()
        for i,j in (0,1),(1,0),(0,-1),(-1,0):
            if n>now_x+i>=0 and m>now_y+j>=0:
                if not visited[now_x+i][now_y+j] and ice_world[now_x+i][now_y+j] > 0:
                    queue.append((now_x+i,now_y+j))
                    visited[now_x+i][now_y+j] = True
                elif ice_world[now_x+i][now_y+j] == 0:
                    count += 1
        icing = max(0,ice_world[now_x][now_y]-count)
        watering.append((now_x,now_y,icing))


# ice_to_water()

result = 0
while True:
    visited = [[False for _ in range(m)]for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if ice_world[i][j] > 0 and not visited[i][j]:
                count += 1
                bfs(i,j)
                
    
    # for i in range(n):
    #     for j in range(m):
    #         if ice_world[i][j] > 0 and not visited[i][j]:
    #             dfs(i,j)
    #             count += 1
    if count > 1:
        break
    elif count == 0:
        result = 0
        break
    for x,y,icing in watering:
        ice_world[x][y] = icing
    watering.clear()
    result += 1

print(result)