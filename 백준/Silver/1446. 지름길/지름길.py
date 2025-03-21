import sys

n,d = map(int,sys.stdin.readline().split())
data = []
for _ in range(n):
    s,e,distance = map(int,sys.stdin.readline().split())
    if e>d or e-s <= distance :
        continue
    data.append((s,e,distance))
    
data.sort()
answer = d

def dak(spot,now_dis,pivot) :
    global answer
    for i in range(pivot+1,len(data)):
        if data[i][0] < spot :
            continue
        dak(data[i][1],now_dis+data[i][0]-spot+data[i][2],i)

    if now_dis + (d-spot) < answer :
        answer = now_dis + (d-spot)
 
for i in range(len(data)):
    spot = data[i][1]
    now_dis = data[i][0] + data[i][2]
    dak(spot,now_dis,i)

print(answer)