from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
result = []
leftMaxheap = [10001]   #max힙은 -로 치환해서 넣어주기
rightMinheap = [10001]
heapq.heapify(leftMaxheap)
heapq.heapify(rightMinheap)
for i in range(1,n+1):
    now = int(sys.stdin.readline())
    if i%2 == 1:
        leftTop = (-1)*leftMaxheap[0]
        rightTop = rightMinheap[0]
        if now > rightTop:
            right = heapq.heappop(rightMinheap)
            right = (-1)*right
            heapq.heappush(leftMaxheap,right)
            heapq.heappush(rightMinheap,now)
        else:
            now = (-1)*now
            heapq.heappush(leftMaxheap,now)
    else :
        leftTop = (-1)*leftMaxheap[0]
        rightTop = rightMinheap[0]
        if leftTop > now :
            leftTop = (-1)*heapq.heappop(leftMaxheap)
            heapq.heappush(rightMinheap,leftTop)
            now = (-1)*now
            heapq.heappush(leftMaxheap,now)
        else :
            heapq.heappush(rightMinheap,now)
    result.append((-1)*leftMaxheap[0])

for i in range(len(result)):
    print(result[i])