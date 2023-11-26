from collections import deque
import sys

a , b, c = map(int,sys.stdin.readline().split())

# max_alpa = max(a,b,c)
# min_alpa = min(a,b,c)
# total = a+b+c
# if a == b == c:
#     print(1)
# elif not a or not b or not c:
#     print(0)
# elif (a+b+c)%6 == 0:
#     if total - max_alpa == min_alpa*2 or total - min_alpa == max_alpa*2 or (min_alpa*2 == total-max_alpa-min_alpa and 2*(total-max_alpa-min_alpa) == max_alpa):
#         print(0)
#     else:
#         print(1)
# else:
#     print(0)

max_num = max(a,b,c)
visited = [[False for _ in range(1501)]for _ in range(1501)]
min_num = min(a,b,c)
total = a+b+c

    
def bfs(max_num,min_num):
    global total
    queue = deque()
    queue.append((max_num,min_num))
    visited[a][b] = True
    while queue:
        x,y = queue.popleft()
        z = total - x - y
        if x == y == z :
            return 1
        for i,j in (x,y),(y,z),(z,x):
            if i == j:
                continue
            elif i>j:
                i -= j
                j *= 2
            else:
                j -= i
                i *= 2
            k = total - i - j
            max_num = max(i,j,k)
            min_num = min(i,j,k)
            if not visited[max_num][min_num]:
                queue.append((max_num,min_num))
                visited[max_num][min_num] = True
    return 0
                    
    
if a == b == c :
    print(1)
elif total%6 == 0: 
    print(bfs(max_num,min_num))
else:
    print(0)