from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

n,k = map(int,sys.stdin.readline().strip().split())
coin = []
visited = [-1 for _ in range(k+1)]

for i in range(n):
    coin.append(int(sys.stdin.readline().strip()))

coin = sorted(coin,reverse=True)

def bfs():
    global k
    queue = deque()
    for i in coin:
        if not i>k:
            if i == k:
                return 1
            else: 
                queue.append([i,1])
                visited[i] = 1
    while queue:
        cost,coin_num = queue.popleft()
        for i in coin:
            if i+cost > k:
                continue
            elif i+cost == k:
                return coin_num+1
            else:
                if visited[i+cost] > coin_num+1 or visited[i+cost] < 0:
                    queue.append([cost+i,coin_num+1])
                    visited[i+cost] = coin_num+1
    return -1

print(bfs())