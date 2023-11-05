from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)
for _ in range(n):
    x = int(sys.stdin.readline())
    heapq.heappush(heap,x)

answer = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum = a+b
    answer += sum
    heapq.heappush(heap,sum)

print(answer)