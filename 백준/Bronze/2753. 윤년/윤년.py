from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
if n%400 == 0:
    print(1)
    sys.exit()
elif n%100 == 0:
    print(0)
    sys.exit()
elif n%4 == 0:
    print(1)
else:
    print(0)