from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

vertex = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
computers = {}
visited = [False for _ in range(vertex+1)]

virus_computer_count = 0

for _ in range(edge):
    v1,v2 = map(int,sys.stdin.readline().strip().split())
    if not v1 in computers:
        computers[v1] = [v2]
    else:
        computers[v1].append(v2)
    if not v2 in computers:
        computers[v2] = [v1]
    else:
        computers[v2].append(v1)


def dfs(start):
    global virus_computer_count
    visited[start] = True
    for i in computers[start]:
        if not visited[i]:
            virus_computer_count += 1
            dfs(i)


if vertex == 1:
    print(0)
else:
    dfs(1)
    print(virus_computer_count)