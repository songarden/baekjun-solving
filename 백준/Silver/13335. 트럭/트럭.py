import sys
from collections import deque


n,w,l = map(int,sys.stdin.readline().split())
# n=트럭수 , w = 다리길이 , L = 다리 하중

queue = deque(list(map(int,sys.stdin.readline().split())))

def func(w,l,n):
    trucksWeight = 0
    time = 0
    inBridge = deque([0 for _ in range(w)])
    while queue:
        time += 1
        trucksWeight -= inBridge.popleft()
        popTruck = queue[0]
        if trucksWeight + popTruck <= l:
            inBridge.append(queue.popleft())
            trucksWeight += popTruck
        else:
            inBridge.append(0)
        
    time = time + w
    
    return time

print(func(w,l,n))