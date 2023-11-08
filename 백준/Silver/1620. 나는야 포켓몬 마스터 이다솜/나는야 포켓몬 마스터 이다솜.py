from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n,m = map(int,sys.stdin.readline().split())
pocketmon = [[]for _ in range(n)]
pocketDict = {}
for i in range(n):
    mon = sys.stdin.readline().strip()
    pocketmon[i].append(mon)
    pocketDict[mon] = i+1


result = []

for _ in range(m):
    str = sys.stdin.readline().strip()
    if str.isdigit():
        result.append(pocketmon[int(str)-1][0])
    else:
        result.append(pocketDict[str])

for ans in result:
    print(ans)