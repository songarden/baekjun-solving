import sys

n, m = map(int,sys.stdin.readline().split())
box = []

for _ in range(n):
    box.append(list(map(int,sys.stdin.readline().split())))

box_add = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        box_add[i+1][j+1] = box[i][j] + box_add[i+1][j]

# print(box_add)
result = [0 for _ in range(m)]
for k in range(m):
    i1,j1, i2,j2 = map(int,sys.stdin.readline().split())
    
    for i in range(i1,i2+1):
        result[k] += box_add[i][j2]-box_add[i][j1-1]

for ans in result:
    print(ans)
