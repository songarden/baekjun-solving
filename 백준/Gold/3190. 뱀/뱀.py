from collections import deque
import copy
import sys
import heapq

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
game_board = [[0 for _ in range(n)] for _ in range(n)]
game = deque()
for i in range(k):
    a, b = map(int,sys.stdin.readline().split())
    game_board[a-1][b-1] = 1
l = int(sys.stdin.readline())
for i in range(l):
    command = list(map(str,sys.stdin.readline().strip().split()))
    game.append(command)


def dummy():
    global n
    go = 1
    time = 0
    boost = False
    head = [0,0]
    game_board[0][0] = 2
    tail = deque()
    tail.append(copy.deepcopy(head))
    end = False
    Direction_time = 0
    commanding = True
    while True:
        if game:
            command = game.popleft()
            Direction_time = int(command[0])-time
        else:
            Direction_time = 100
            commanding = False
        for _ in range(0,Direction_time):
            time += 1
            if go == 1:
                head[1] += 1
                tail.append(copy.deepcopy(head))
                if head[1] > n-1: #벽일 때
                    end =True
                    break
                elif game_board[head[0]][head[1]] == 1: #사과일 때
                    boost = True
                elif game_board[head[0]][head[1]] == 2: #자기 몸일 때
                    end=True
                    break
                game_board[head[0]][head[1]] = 2
                if not boost:
                    tail_dir = tail.popleft()
                    game_board[tail_dir[0]][tail_dir[1]] = 0

            elif go == 2:
                head[0] += 1
                tail.append(copy.deepcopy(head))
                if head[0] > n-1:
                    end=True
                    break
                elif game_board[head[0]][head[1]] == 1: #사과일 때
                    boost = True
                elif game_board[head[0]][head[1]] == 2: #자기 몸일 때
                    end=True
                    break
                game_board[head[0]][head[1]] = 2
                if not boost:
                    tail_dir = tail.popleft()
                    game_board[tail_dir[0]][tail_dir[1]] = 0

            elif go == 3:
                head[1] -= 1
                tail.append(copy.deepcopy(head))
                if head[1] < 0:
                    end=True
                    break
                elif game_board[head[0]][head[1]] == 1: #사과일 때
                    boost = True
                elif game_board[head[0]][head[1]] == 2: #자기 몸일 때
                    end=True
                    break
                game_board[head[0]][head[1]] = 2
                if not boost:
                    tail_dir = tail.popleft()
                    game_board[tail_dir[0]][tail_dir[1]] = 0
                
            elif go == 0:
                head[0] -= 1
                tail.append(copy.deepcopy(head))
                if head[0] < 0:
                    end=True
                    break
                elif game_board[head[0]][head[1]] == 1: #사과일 때
                    boost = True
                elif game_board[head[0]][head[1]] == 2: #자기 몸일 때
                    end=True
                    break
                game_board[head[0]][head[1]] = 2
                if not boost:
                    tail_dir = tail.popleft()
                    game_board[tail_dir[0]][tail_dir[1]] = 0
            boost = False
        if end:
            break
        if commanding and command[1] == 'D':
            go = (go+1)%4
        elif commanding and command[1] == 'L':
            if go == 0:
                go = 3
            else :
                go = (go-1)%4
    return time

print(dummy())