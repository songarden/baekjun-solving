from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if x>0:
    if y>0:
        print(1)
    else:
        print(4)
else:
    if y>0:
        print(2)
    else:
        print(3)