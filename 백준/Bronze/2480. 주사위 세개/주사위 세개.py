from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

a , b , c = map(int,sys.stdin.readline().split())
if a == b:
    if b == c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
elif b == c:
    print(1000+b*100)
elif c == a:
    print(1000+a*100)
else:
    max_num = max(a,b,c)
    print(100*max_num)