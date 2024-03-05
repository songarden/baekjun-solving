import sys
import heapq


n, k = map(int,sys.stdin.readline().split())
visited = [-1 for _ in range(100001)]

def play(n,bro):
    if n >= bro:
        return (n - bro)
    heap = []
    heapq.heapify(heap)
    if n != 0:
        heapq.heappush(heap, (0,n))
        visited[n] = 0
    else :
        heapq.heappush(heap, (1,1))
        visited[1] = 1
        visited[0] = 0
        

    while(heap):
        time , thisN = heapq.heappop(heap)
        temp = thisN
        while(True):
            if temp > bro :
                break
            temp *= 2
            if temp > 100000:
                break
            if visited[temp] <= time and visited[temp] != -1 :
                break
            if temp == bro:
                return time
            heapq.heappush(heap,(time,temp))
            visited[temp] = time
        
        if thisN != 0:
            if thisN == bro :
                return time
            if thisN+1 == bro or thisN-1 == bro:
                return time +1
            
        for i in -1,1:
            if 100000 >= thisN+i > 0 :
                if visited[thisN+i] == -1 or visited[thisN+i] > time+1:
                    visited[(thisN+i)] = time + 1
                    heapq.heappush(heap,(time+1,thisN+i))

print(play(n,k))