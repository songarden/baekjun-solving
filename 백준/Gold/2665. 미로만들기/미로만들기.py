from collections import deque
import sys
import heapq

n = int(sys.stdin.readline())

rooms = []

for _ in range(n):
    rooms.append(list(map(int,sys.stdin.readline().strip())))

for i in range(n):
    for j in range(n):
        if rooms[i][j] == 0:
            rooms[i][j] = 1
        elif rooms[i][j] == 1:
            rooms[i][j] = 0

def room_for_dijkstra(startX,startY):
    global n
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap,[rooms[startX][startY],startX,startY])
    while heap:
        this = heapq.heappop(heap)  #[룸의[x][y] 값 (비용) ,  x인덱스, y인덱스]
        
        for i,j in (0,1),(1,0),(0,-1),(-1,0):
            if this[1]+i>=n or this[1]+i<0 or this[2]+j>=n or this[2]+j<0:
                continue
            if rooms[this[1]+i][this[2]+j] < 0:
                continue
            if this[1]+i == n-1 and this[2]+j == n-1 :
                return rooms[n-1][n-1]+this[0]
            rooms[this[1]+i][this[2]+j] += this[0]
            heapq.heappush(heap,[rooms[this[1]+i][this[2]+j],this[1]+i,this[2]+j])
        
        rooms[this[1]][this[2]] = -10
    
answer = room_for_dijkstra(0,0)
print(answer)