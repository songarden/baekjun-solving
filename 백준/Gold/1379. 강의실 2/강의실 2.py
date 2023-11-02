import sys
import heapq

n = int(sys.stdin.readline())

classInfo = []

classroom = [0 for _ in range(n+1)]

for _ in range(n):
    classNum , start , end = map(int,sys.stdin.readline().split())
    classInfo.append((start,end,classNum))
classInfo.sort()
heap = []
heapq.heapify(heap)
class_count = 0
for i in range(n):
    this_start,this_end,this_class = classInfo[i]
    if not heap:
        class_count += 1
        heapq.heappush(heap,(this_end,class_count))
        classroom[this_class] = class_count
    else:
        if heap[0][0] <= this_start:
            bef_end,bef_class = heapq.heappop(heap)
            heapq.heappush(heap,(this_end,bef_class))
            classroom[this_class] = bef_class
        else:
            class_count += 1
            heapq.heappush(heap,(this_end,class_count))
            classroom[this_class] = class_count

print(class_count)
for i in range(1,len(classroom)):
    print(classroom[i])