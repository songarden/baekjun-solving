from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)

n , m = map(int,sys.stdin.readline().strip().split())

graph = [[0 for _ in range(n)]for _ in range(n)]
graph_bigger = [0 for _ in range(n)]
graph_smaller = [0 for _ in range(n)]
for _ in range(m):
    big , small = map(int,sys.stdin.readline().strip().split())
    if graph[big-1][small-1] == 0:
        graph[big-1][small-1] = -1
        graph[small-1][big-1] = 1
        graph_smaller[big-1] += 1
        graph_bigger[small-1] += 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or j == k:
                continue
            elif graph[j][k] == 1 and graph[k][i] == 1 and graph[j][i] == 0:
                graph_bigger[j] += 1
                graph[j][i] = 1
            elif graph[j][k] == -1 and graph[k][i] == -1 and graph[j][i] == 0:
                graph_smaller[j] += 1
                graph[j][i] = -1

result = 0

for i in range(n):
    if abs(graph_smaller[i]) > n//2 :
        result += 1
    elif abs(graph_bigger[i]) > n//2 :
        result += 1

print(result)