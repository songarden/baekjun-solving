from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
outdegree = [0 for _ in range(n+1)]
partGlobalNum = [0 for _ in range(n+1)]
toys = {}
result = []
for _ in range(m):
    toy , part_toy, num = map(int,sys.stdin.readline().strip().split())
    if not toy in toys:
        toys[toy] = [(part_toy,num)]
    else:
        toys[toy].append((part_toy,num))
    outdegree[part_toy] += 1

def bfs_toy():
    global n
    queue = deque()
    queue.append((n,1))
    while queue:
        nowToy,nowMustNumber = queue.popleft()
        if not nowToy in toys:
            result.append([nowToy,nowMustNumber])
        else:
            for partToy,partNum in toys[nowToy]:
                partGlobalNum[partToy] += partNum*nowMustNumber
                outdegree[partToy] -= 1
                if outdegree[partToy] == 0:
                    queue.append((partToy,partGlobalNum[partToy]))

bfs_toy()
result = sorted(result)
for ans in result:
    print(' '.join(list(map(str,ans))))