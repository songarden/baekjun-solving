from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n,k = map(int,sys.stdin.readline().split())
number = sys.stdin.readline().strip()
# numList = [int(num) for num in number].reverse()
pop_count = 0
stack = []

sliced_index = 0
for i in range(n):
    while pop_count < k:
        if not stack:
            stack.append(int(number[i]))
            break
        elif int(number[i]) <= stack[-1]:
            stack.append(int(number[i]))
            break
        else:
            stack.pop()
            pop_count += 1

    if pop_count == k:
        sliced_index = i
        break
while len(stack) > n-k :
    stack.pop()
    sliced_index = n+1    
for i in range(sliced_index,n):
    stack.append(int(number[i]))
if len(stack) >= 2:
    for i in range(len(stack)-1):
        print(stack[i],end='')
print(stack[-1])