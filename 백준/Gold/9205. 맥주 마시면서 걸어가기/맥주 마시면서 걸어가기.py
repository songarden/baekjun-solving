import sys
from collections import deque

testcase = int(sys.stdin.readline())
result = []

for _ in range(testcase):
    market = int(sys.stdin.readline())
    homeX, homeY = map(int,sys.stdin.readline().split())
    queue = deque()
    queue.append((homeX,homeY))
    marketPlace = []
    for i in range(market):
        a,b = map(int,sys.stdin.readline().split())
        marketPlace.append([a,b])
    visited = [False for _ in range(market)]
    endX, endY = map(int,sys.stdin.readline().split())
    goal = False
    while(queue) :
        x , y = queue.popleft()
        if abs(endX - x) + abs(endY - y) <= 1000:
            goal = True
            break
        else:
            for i in range(market):
                if not visited[i] and abs(marketPlace[i][0] - x) + abs(marketPlace[i][1] - y) <= 1000:
                    queue.append((marketPlace[i][0],marketPlace[i][1]))
                    visited[i] = True
    if goal :
        print("happy")
    else:
        print("sad")
                

    
    
    