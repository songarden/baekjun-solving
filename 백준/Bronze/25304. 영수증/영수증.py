from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)

ans = int(sys.stdin.readline())
test = int(sys.stdin.readline())
temp = 0
for _ in range(test):
    m , c = map(int,sys.stdin.readline().split())
    temp += m*c

if ans == temp :
    print("Yes")
else:
    print("No")