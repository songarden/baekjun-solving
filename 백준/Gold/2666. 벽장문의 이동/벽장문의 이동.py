import sys
from collections import deque

n = int(sys.stdin.readline())
e1, e2 = map(int,sys.stdin.readline().split())
test = int(sys.stdin.readline())
caseList = []
for _ in range(test):
    caseList.append(int(sys.stdin.readline()))

queue = deque()
index = 0
move = 0
queue.append((e1,e2,index,move))
minMove = float('inf')

while(queue):
    ea,eb,id,mv = queue.popleft()
    if mv > minMove :
        continue
    if id == test-1:
        minMove = min(minMove,mv+min(abs(ea-caseList[id]),abs(eb-caseList[id])))
        # print("Last emptyDoor is ",ea,eb,"minMove = ",minMove)
        continue
    
    if (ea - caseList[id]) * (eb - caseList[id]) < 0 :
        # print("case 0, idx = ",id,"emptyDoor is ",ea,eb)
        queue.append((ea,caseList[id],id+1,mv+abs(caseList[id] - eb)))
        queue.append((caseList[id],eb,id+1,mv+abs(caseList[id] - ea)))
        # print(queue)
        
    elif abs(caseList[id] - ea) < abs(caseList[id] - eb):
        # print("case 1, idx = ",id,"emptyDoor is ",ea,eb)
        queue.append((caseList[id],eb,id+1,mv+abs(caseList[id] - ea)))
        # print(queue)
    elif abs(caseList[id] - ea) > abs(caseList[id] - eb):
        # print("case 2, idx = ",id,"emptyDoor is ",ea,eb)
        queue.append((ea,caseList[id],id+1,mv+abs(caseList[id] - eb)))
        # print(queue)


print(minMove)