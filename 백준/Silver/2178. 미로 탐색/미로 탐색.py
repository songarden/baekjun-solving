from collections import deque
import sys

n , m = map(int, sys.stdin.readline().strip().split())
maze = []
for i in range(n):
    maze.append(list(map(int,sys.stdin.readline().strip())))

def bfs(i,j):
    global n
    global m
    queue = deque()
    queue.append([i,j,1])
    while queue:
        now = queue.popleft()
        if now[0] == n-1 and now[1] == m-1: #목적지에 도착했을 때 함수 종료
            return now[2]
        
        if not now[1] == m-1 :
            if maze[now[0]][now[1]+1] == 1:
                queue.append([now[0],now[1]+1,now[2]+1])
                maze[now[0]][now[1]+1] = 0

        if not now[0] == n-1 :
            if maze[now[0]+1][now[1]] == 1:
                queue.append([now[0]+1,now[1],now[2]+1])
                maze[now[0]+1][now[1]] = 0

        if not now[1] == 0 :
            if  maze[now[0]][now[1]-1] == 1:
                queue.append([now[0],now[1]-1,now[2]+1])

        if not now[0] == 0 :
            if  maze[now[0]-1][now[1]] == 1:
                queue.append([now[0]-1,now[1],now[2]+1])
                maze[now[0]-1][now[1]] = 0
        
        
print(bfs(0,0))