import sys
cost = 0
n = int(sys.stdin.readline())
min = 1000000*n+1
graph = []
visited = [False]*n
all_True = False
for i in range(n):
    way = list(map(int,sys.stdin.readline().strip().split()))
    graph.append(way)

def travel(graph,here,start):
    global cost
    global min
    global all_True
    n = len(graph[here])
    for i in range(n):
        if (visited[i] == False
            and not graph[here][i] == 0
            and not i == start) :
            cost += graph[here][i]
            visited[i] = True
            travel(graph,i,start)
            cost -= graph[here][i]
            visited[i] = False
    for i in range(n):
        if not visited[i] and not i == start :
            all_True = False
            break
        all_True = True
    
    
    if all_True and not graph[here][start] == 0 :
        cost += graph[here][start]
        if cost < min and not here == start :
            min = cost
        cost -= graph[here][start]

travel(graph,0,0)

print(min)