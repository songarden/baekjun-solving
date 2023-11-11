from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)



while True:
    a, b= map(int,sys.stdin.readline().split())
    if a == 0 and b == 0:
        sys.exit()
    print(a+b)