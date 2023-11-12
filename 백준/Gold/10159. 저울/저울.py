import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

map_list = [[0 for _ in range(n+1)] for _ in range(n+1)]
ans = [n-1 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    map_list[a][b] = 1
    # ans[a] += 1
    # ans[b] += 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if map_list[i][k] == 1 and map_list[k][j] == 1:
                map_list[i][j] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        if map_list[i][j] == 1:
            ans[i] -= 1
            ans[j] -= 1 
            
                
for i in range(1,n+1):
    count = ans[i]
    print(count)