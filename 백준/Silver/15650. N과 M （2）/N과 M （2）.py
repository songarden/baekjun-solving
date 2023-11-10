from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)

n,r = map(int,sys.stdin.readline().split())

list_num = [i for i in range(1,n+1)]
ans = permutations(list_num,r)

ans_2 = list(set(tuple(sorted(res)) for res in ans))
ans_2.sort()
for res in ans_2:
    print(*res)