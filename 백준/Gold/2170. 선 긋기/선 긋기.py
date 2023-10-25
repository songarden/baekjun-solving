import sys

n = int(sys.stdin.readline())
line = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().strip().split())
    line.append((x,y))

line = sorted(line)
space = 0
now = 0
for i in range(n):
    if i == 0:
        now = line[i][1]
    else:
        if now < line[i][0]:
            space += line[i][0] - now
            now = line[i][1]
        else :
            now = max(now,line[i][1])

print(now-line[0][0]-space)