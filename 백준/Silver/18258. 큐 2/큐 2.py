import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline())
for i in range(n):
    command = list(map(str,sys.stdin.readline().strip().split()))
    if command[0] == "push":
        item = int(command[1])
        queue.append(item)
    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            item = queue.popleft()
            print(item)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])