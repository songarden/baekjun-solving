import sys
import math



x,y,w,s = map(int,sys.stdin.readline().split())
min_di = min(x,y)
max_di = max(x,y)
if 2*w <= s:
    print((x+y)*w)
elif w < s < 2*w :
    answer = (min_di*s)+ abs(x-y)*w
    print(answer)
elif s <= w:
    if (min_di+max_di)%2 == 1:
        print((max_di-1)*s + w)
    else:
        print(max_di*s)