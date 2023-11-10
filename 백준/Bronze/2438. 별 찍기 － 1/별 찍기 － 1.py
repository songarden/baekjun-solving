from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

for i in range(n):
    print("*"*(i+1))