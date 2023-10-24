from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline().strip())
num_list = list(map(int,sys.stdin.readline().strip().split()))
plus,minus,mul,div = map(int,sys.stdin.readline().strip().split())

math_task_list = []
for i in range(plus):
    math_task_list.append("+")
for i in range(minus):
    math_task_list.append("-")
for i in range(mul):
    math_task_list.append("*")
for i in range(div):
    math_task_list.append("/")

math_task_list = list(set(permutations(math_task_list)))
# print(num_list)
# print(math_task_list)
INF = float('inf')
result = [INF,-1*(INF)]
for i in range(len(math_task_list)):
    temp = num_list[0]
    temp_list = math_task_list[i]
    for j in range(n-1):
        if temp_list[j] == '+':
            temp += num_list[j+1]
        elif temp_list[j] == '-':
            temp -= num_list[j+1]
        elif temp_list[j] == '*':
            temp *= num_list[j+1]
        elif temp_list[j] == '/':
            if temp >= 0 :
                temp //= num_list[j+1]
            else:
                temp = -1*((-1*(temp))//num_list[j+1])
    result[0] = min(result[0],temp)
    result[1] = max(result[1],temp)

for i in range(1,-1,-1):
    print(result[i])