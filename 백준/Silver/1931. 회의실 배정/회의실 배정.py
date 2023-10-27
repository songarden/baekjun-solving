from collections import deque
import copy
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)
endTime = 0
for i in range(n):
    start , end = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,(start,end))
bookingLog = []
while heap:
    start, end = heapq.heappop(heap)
    if not bookingLog:
        bookingLog.append([start,end])
    else:
        if bookingLog[-1][1] > end:
            bookingLog.pop()
            bookingLog.append([start,end])
        elif bookingLog[-1][1] <= start:
            bookingLog.append([start,end])

# print(bookingLog)
print(len(bookingLog))