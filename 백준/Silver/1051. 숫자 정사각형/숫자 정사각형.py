from collections import deque
import copy
import sys
import heapq
import math
sys.setrecursionlimit(10**6)

n , m = map(int,sys.stdin.readline().split())

num_map = []
for _ in range(n):
    num_map.append(list(map(int,sys.stdin.readline().strip())))

min_line = min(n,m)
max_line = max(n,m)

for k in range(min_line-1,0,-1):
    for i in range(0,n - k):
        for j in range(0,m - k):
            if num_map[i][j] == num_map[i+k][j] == num_map[i][j+k] == num_map[i+k][j+k]:
                print((k+1)**2)
                sys.exit()
            
print(1)