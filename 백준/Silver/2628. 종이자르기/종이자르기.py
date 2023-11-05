from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

j,i = map(int,sys.stdin.readline().split())

cutCount = int(sys.stdin.readline())
row = [0,j]
col = [0,i]

for _ in range(cutCount):
    n , cutNum = map(int,sys.stdin.readline().split())
    if n == 1:
        row.append(cutNum)
    else:

        col.append(cutNum)

if cutCount == 0:
    print(i*j)
    sys.exit()


row.sort()
col.sort()
maxRow = row[1]-row[0]
maxCol = col[1]-col[0]
for l in range(2,len(row)):
    maxRow = max(maxRow,row[l]-row[l-1])

for l in range(2,len(col)):
    maxCol = max(maxCol,col[l]-col[l-1])

print(maxRow*maxCol)