from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)


try:
    while True:
        a, b= map(int,sys.stdin.readline().split())
        print(a+b)
except Exception:
    sys.exit()