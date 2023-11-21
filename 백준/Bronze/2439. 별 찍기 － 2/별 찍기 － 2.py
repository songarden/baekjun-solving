from collections import deque
import copy
import sys
import heapq
import math
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(' '*(n-i)+ '*'*i)