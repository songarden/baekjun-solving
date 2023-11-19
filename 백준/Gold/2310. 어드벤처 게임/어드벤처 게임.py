from collections import deque
import heapq
import sys

def func(start,end,rooms,visitedCost):
    cost = 0
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap,(-1*cost,start))
    visitedCost[start] = cost
    while heap:
        reverseCost , nowIndex = heapq.heappop(heap)
        nowCost = -1 *reverseCost
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
            if visitedCost[int(rooms[nowIndex-1][i])] < nowCost and not int(rooms[nowIndex-1][i]) == nowIndex:
                heapq.heappush(heap,(-1*nowCost , int(rooms[nowIndex-1][i])))
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