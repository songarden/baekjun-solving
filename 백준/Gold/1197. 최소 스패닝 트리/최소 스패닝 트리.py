from collections import deque
import sys
import heapq
edges = []
v, e = map(int,sys.stdin.readline().strip().split())
for i in range(e):
    v1 , v2 , cost = map(int,sys.stdin.readline().strip().split())
    edges.append((cost,v1,v2))

edges.sort()
p = []
for i in range(v+1):
    p.append(i)


def find_parend(v):
    if not p[v] == v:
        p[v] = find_parend(p[v]) 
    return p[v]

def mst():
    global v
    global e
    sum = 0
    for edge in edges:
        cost , v1, v2 = edge
        p1 = find_parend(v1)
        p2 = find_parend(v2)
        if not p1 == p2:
            if p1 >= p2:
                p[p2] = p1
            else :
                p[p1] = p2
            sum += cost
    return sum
answer = mst()
print(answer)