import sys


stack = []
n = int(sys.stdin.readline())
for i in range(n):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if command[0] == "push":
        num = int(command[1])
        stack.append(num)
    elif command[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if not stack :
            print(1)
        else:
            print(0)
    elif command[0] == "pop":
        if not stack :
            print(-1)
        else:
            num = stack.pop()
            print(num)