import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

counted = [False for _ in range(n+1)]
dict = {}

answer = 0
for i in range(m):
    f1 , f2 = map(int,sys.stdin.readline().split())
    
    if not f1 in dict:
        dict[f1] = [f2]
    else:
        dict[f1].append(f2)
    if not f2 in dict:
        dict[f2] = [f1]
    else:
        dict[f2].append(f1)
counted[1] = True
queue = deque()
if not 1 in dict:
    print(0)
    sys.exit()
for item in dict[1]:
    queue.append(item)
    answer += 1
    counted[item] = True
    
while(queue):
    num = queue.popleft()
    for friend in dict[num]:
        if not counted[friend]:
            counted[friend] = True
            answer += 1

print(answer)
        