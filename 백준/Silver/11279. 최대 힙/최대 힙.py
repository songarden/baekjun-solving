from collections import deque
import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
heapq.heapify(max_heap)
for i in range(n):
    n = int(sys.stdin.readline())
    if n == 0:
        if not max_heap:
            print(0)
        else:
            key = heapq.heappop(max_heap)
            key *= -1
            print(key)
    else:
        heapq.heappush(max_heap,(-1)*n)