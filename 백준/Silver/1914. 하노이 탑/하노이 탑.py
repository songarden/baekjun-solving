import sys


moving = []

def hanoii(n,start,goal,extra):
    if n>1 :
        hanoii(n-1,start,extra,goal)
    print(start,goal)
    if n>1 :
        hanoii(n-1,extra,goal,start)

n = int(sys.stdin.readline())
result = 1
for i in range(1,n) :
    result = result + result + 1
if n<=20 :
    print(result)
    hanoii(n,1,3,2)
else :
    print(result)