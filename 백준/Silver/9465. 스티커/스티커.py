from collections import deque
import sys
import math



t = int(sys.stdin.readline());
answer = []
for i in range(t):
    n = int(sys.stdin.readline())
    numList = []
    for _ in range(2):
        numList.append(list(map(int,sys.stdin.readline().split())))
    for j in range(1,n):
        for k in range(2):
            if j == 1:
                numList[k][j] += numList[(k+1)%2][j-1]
            else:
                maxHere = 0
                for di,dj in (0,-1),(0,-2),(1,-1),(1,-2):
                    if k == di and dj == -1:
                        continue
                    else:
                        maxHere = max(maxHere , numList[di][j+dj])
                numList[k][j] += maxHere
    answer.append(max(numList[0][n-1],numList[1][n-1]))

for ans in answer:
    print(ans)