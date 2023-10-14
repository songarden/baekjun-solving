import sys
input = sys.stdin.readline

T = int(input())

# 답은 0, 1, 2중에 하나다
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    isSameNode = False
    if (x1 == x2) and (y1 == y2):
        isSameNode = True
    
    # 두 노드의 좌표가 같을 때
    if isSameNode:
        if r1 != r2:
            print(0)
        else:
            if r1 == 0 :
                print(1)
            else :
                print(-1)
    # 두 노드의 좌표가 다를 때
    else:
        distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        if (r1 + r2 == distance) or (abs(r1 - r2) == distance):
            print(1)
        elif abs(r1 - r2) < distance < (r1 + r2):
            print(2)
        else:
            print(0)