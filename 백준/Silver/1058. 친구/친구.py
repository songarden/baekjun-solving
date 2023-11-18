from collections import deque
import copy
import sys
import heapq
import math
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
friends = []
answer = {}
for _ in range(n):
    friends.append(list(map(str,sys.stdin.readline().strip())))

for k in range(n):
    answer[k] = []
    for i in range(n):
        if not friends[k][i] == 'Y':
            continue
        else:
            answer[k].append(i)
        for j in range(n):
            if k == j or friends[k][j] == 'Y':
                continue
            if friends[k][i] == friends[i][j] == 'Y':
                answer[k].append(j)

max_count = 0       
for key in answer.keys():
    new = set(answer[key])
    max_count = max(len(new),max_count)


print(max_count)