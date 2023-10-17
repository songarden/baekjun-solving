import sys


n = int(sys.stdin.readline())
result = []
building = list(map(int,sys.stdin.readline().split()))

stack = []

for i in range(n):
    while stack:
        if building[stack[-1]] < building[i]:
            stack.pop()
        else:
            result.append(stack[-1]+1)
            stack.append(i)
            break
    
    if not stack:
        stack.append(i)
        result.append(0)
    
    
    
    

print(' '.join(map(str,result)))