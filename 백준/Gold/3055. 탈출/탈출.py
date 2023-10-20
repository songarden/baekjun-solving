from collections import deque
import sys

r , s = map(int,sys.stdin.readline().strip().split())
forest = []
for _ in range(r):
    forest.append(list(map(str,sys.stdin.readline().strip())))
# print(forest)


def escape_with_bfs():
    global r
    global s
    water_task_num = 0
    boy_task_num = 0
    boy_queue = deque()
    water_queue = deque()
    for i in range(r):
        for j in range(s):
            if forest[i][j] == 'S':
                boy_queue.append([i,j,0])
                boy_task_num += 1
            if forest[i][j] == '*':
                water_queue.append([i,j])
                water_task_num += 1
    
    while boy_queue:
        temp = water_task_num
        water_task_num = 0
        for i in range(temp):
            water = water_queue.popleft()
            if not water[1] >= s-1: 
                if forest[water[0]][water[1]+1] == '.':
                    forest[water[0]][water[1]+1] = '*'
                    water_task_num += 1
                    water_queue.append([water[0],water[1]+1])
            if not water[0] >= r-1:
                if forest[water[0]+1][water[1]] == '.':
                    forest[water[0]+1][water[1]] = '*'
                    water_task_num += 1
                    water_queue.append([water[0]+1,water[1]])
            if not water[1] == 0:
                if forest[water[0]][water[1]-1] == '.':
                    forest[water[0]][water[1]-1] = '*'
                    water_task_num += 1
                    water_queue.append([water[0],water[1]-1])
            if not water[0] == 0:
                if forest[water[0]-1][water[1]] == '.':
                    forest[water[0]-1][water[1]] = '*'
                    water_task_num += 1
                    water_queue.append([water[0]-1,water[1]])

        temp = boy_task_num
        boy_task_num = 0
        for i in range(temp):
            boy = boy_queue.popleft()
            if not boy[1] >= s-1:
                if forest[boy[0]][boy[1]+1] == 'D':
                    return boy[2]+1
                elif forest[boy[0]][boy[1]+1] == '.':
                    forest[boy[0]][boy[1]+1] = 'S'
                    boy_queue.append([boy[0],boy[1]+1,boy[2]+1])
                    boy_task_num += 1
            if not boy[0] >= r-1:
                if forest[boy[0]+1][boy[1]] == 'D':
                    return boy[2]+1
                elif forest[boy[0]+1][boy[1]] == '.':
                    forest[boy[0]+1][boy[1]] = 'S'
                    boy_queue.append([boy[0]+1,boy[1],boy[2]+1])
                    boy_task_num += 1
            if not boy[1] == 0:
                if forest[boy[0]][boy[1]-1] == 'D':
                    return boy[2]+1
                elif forest[boy[0]][boy[1]-1] == '.':
                    forest[boy[0]][boy[1]-1] = 'S'
                    boy_queue.append([boy[0],boy[1]-1,boy[2]+1])
                    boy_task_num += 1
            if not boy[0] == 0:
                if forest[boy[0]-1][boy[1]] == 'D':
                    return boy[2]+1
                elif forest[boy[0]-1][boy[1]] == '.':
                    forest[boy[0]-1][boy[1]] = 'S'
                    boy_queue.append([boy[0]-1,boy[1],boy[2]+1])
                    boy_task_num += 1
    return "KAKTUS"

answer = escape_with_bfs()
print(answer)