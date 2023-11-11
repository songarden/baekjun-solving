from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)


n = sys.stdin.readline()
a = sys.stdin.readline().strip()

listup = [int(num) for num in a]
ans = 0
for nums in listup:
    ans += nums

print(ans)