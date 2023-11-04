from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

h , m = map(int,sys.stdin.readline().split())
p_m = int(sys.stdin.readline())
p_h = 0
if p_m > 59:
    p_h = p_m//60
    p_m = p_m%60

if p_m+m > 59:
    h += 1
    m = p_m + m - 60
    p_m = 0

print((p_h+h)%24,m+p_m)