import sys

stack = []

k = int(sys.stdin.readline())

for _ in range(k):
    i = int(sys.stdin.readline())
    if not i:
        stack.pop()
    else:
        stack.append(i)
answer = 0
for ans in stack:
    answer += ans
    
print(answer)