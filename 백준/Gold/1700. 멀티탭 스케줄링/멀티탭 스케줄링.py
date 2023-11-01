from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n,k = map(int,sys.stdin.readline().split())

items = list(map(int,sys.stdin.readline().split()))
i = 0
pluged_items = []
for item in items:
    i += 1
    if not item in pluged_items:
        pluged_items.append(item)
        if len(pluged_items) == n:
            break


other_task = items[i:]
count = 0

for m in range(len(other_task)):
    if other_task[m] in pluged_items:
        continue
    else:
        pluged_important_cost = [k for _ in range(n)]
        for i in range(len(pluged_items)):
            for item_index in range(m,len(other_task)):
                if other_task[item_index] == pluged_items[i]:
                    pluged_important_cost[i] = item_index
                    break

        pluged_items[pluged_important_cost.index(max(pluged_important_cost))] = other_task[m]
        count += 1

print(count)