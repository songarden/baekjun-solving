import sys
import heapq

n = int(sys.stdin.readline())
ways = []
for _ in range(n):
    x,y = map(int,sys.stdin.readline().strip().split())
    if x > y:
        x,y = y,x
    ways.append((x,y))

l = int(sys.stdin.readline())

ways = sorted(ways)

result = 0
lx = ways[0][0]
ly = lx+l
heap = []
heapq.heapify(heap)
ways = sorted(ways,key = lambda x :x[1])

for i in range(len(ways)):
    way_x, way_y = ways[i]
    if way_y - way_x > l:
        continue

    if way_y <= ly :
        heapq.heappush(heap,way_x)
    else :
        ly = way_y
        lx = way_y - l
        while heap:
            if heap[0] < lx:
                heapq.heappop(heap)
            else :
                break
        heapq.heappush(heap,way_x)
    result = max(result,len(heap))
        

print(result)