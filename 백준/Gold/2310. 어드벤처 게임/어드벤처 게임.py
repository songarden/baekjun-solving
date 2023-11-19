from collections import deque
import sys


def func(start,end,rooms,visitedCost):
    cost = 0
    queue = deque()
    queue.append((start,cost))
    visitedCost[start] = cost
    while queue:
        nowIndex , nowCost = queue.popleft()
        alpha = rooms[nowIndex-1][0]
        roomCost = int(rooms[nowIndex-1][1])
        
        if alpha == 'L':
            if nowCost < roomCost:
                nowCost = roomCost
        elif alpha == 'T':
            nowCost -= roomCost
            if nowCost < 0:
                continue
        if nowIndex == end:
            return 'Yes'
        i = 2
        while rooms[nowIndex-1][i] != '0' :
            if visitedCost[int(rooms[nowIndex-1][i])] < nowCost:
                queue.append((int(rooms[nowIndex-1][i]) , nowCost))
                visitedCost[int(rooms[nowIndex-1][i])] = nowCost
            i += 1
    return 'No'
            
        

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    visitedCost = [-1 for _ in range(n+1)]
    rooms = []
    for _ in range(n):
        rooms.append(list(map(str,sys.stdin.readline().rstrip().split())))
    
    print(func(1,n,rooms,visitedCost))