from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)

testCase = int(sys.stdin.readline().strip())
result = ['YES' for _ in range(testCase)]
colorOne = 'Blue'
colorTwo = 'Red'


    
for i in range(testCase):
    v,e = map(int,sys.stdin.readline().strip().split())
    color = ['White' for _ in range(v+1)]
    graph = {}
    for _ in range(e):
        v1 ,v2 = map(int,sys.stdin.readline().strip().split())
        if not v1 in graph:
            graph[v1] = [v2]
        else:
            graph[v1].append(v2)
        if not v2 in graph:
            graph[v2] = [v1]
        else:
            graph[v2].append(v1)

    def dfs(v,This_color,testCase):
        global colorOne
        global colorTwo
        color[v] = This_color
        anotherCor = 'White'
        if colorOne == This_color:
            anotherCor = colorTwo
        else:
            anotherCor = colorOne
        for next in graph[v]:
            if color[next] == 'White' :
                dfs(next,anotherCor,testCase)
            elif color[next] == color[v]:
                result[testCase] = 'NO'

    if v == 1:
        result[testCase] = 'NO'
        continue
    for j in graph.keys():
        if color[j] == 'White':
            dfs(j,colorOne,i)

for j in range(testCase):
    print(result[j])