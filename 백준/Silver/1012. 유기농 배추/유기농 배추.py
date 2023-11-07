from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)



t = int(sys.stdin.readline())
result = [0 for _ in range(t)]
for k in range(t):
    n , m , baechu = map(int,sys.stdin.readline().split())
    baechu_map = [[0 for _ in range(n)]for _ in range(m)]
    visited = [[False for _ in range(n)]for _ in range(m)]
    for _ in range(baechu):
        j,i = map(int,sys.stdin.readline().split())
        baechu_map[i][j] = 1
    
    def baechu_dfs(i,j,n,m):
        visited[i][j] = True
        for di,dj in (0,1),(1,0),(0,-1),(-1,0):
            if m>i+di>=0 and n>j+dj>=0:
                if not visited[i+di][j+dj] and baechu_map[i+di][j+dj] == 1:
                    baechu_dfs(i+di,j+dj,n,m)
    

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and baechu_map[i][j] == 1:
                baechu_dfs(i,j,n,m)
                result[k] += 1

for ans in result:
    print(ans)