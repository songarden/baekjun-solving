import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
INF = float('inf')
manmap = {}
man1 , man2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if not a in manmap:
        manmap[a] = [b]
    else:
        manmap[a].append(b)
    if not b in manmap:
        manmap[b] = [a]
    else:
        manmap[b].append(a)

visited = [False for _ in range(n+1)]
result = INF
def dfs(src , cnt, dst,isTrue) :
    global result
    global n
    if dst in manmap[src]:
        result = min(cnt+1,result)
        return True
    for i in manmap[src]:
        if not visited[i]:
            visited[i] = True
            isTrue = dfs(i,cnt+1,dst,isTrue)
            visited[i] = False
    return isTrue

correct = dfs(man1,0,man2,False)
if not correct :
    print(-1)
else:      
    print(result)