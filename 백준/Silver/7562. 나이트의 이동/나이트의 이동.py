import sys
from collections import deque


testCase = int(sys.stdin.readline())

def chessNightMove(n,startI,startJ,endI,endJ):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((startI,startJ,0))
    visited[startI][startJ] = True
    
    while(queue):
        i,j,cnt = queue.popleft()
        if i==endI and j==endJ:
            return cnt
        for di,dj in (1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1):
            if n>di+i>=0 and n>dj+j>=0:
                if not visited[di+i][dj+j]:
                    visited[di+i][dj+j] = True
                    queue.append((di+i,dj+j,cnt+1))
    


for i in range(testCase):
    n = int(sys.stdin.readline())
    
    startI, startJ = map(int,sys.stdin.readline().split())
    endI, endJ = map(int,sys.stdin.readline().split())
    print(chessNightMove(n,startI,startJ,endI,endJ))
    


    