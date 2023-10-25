from collections import deque
from itertools import permutations
import sys
import heapq
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())
result = []
result_num = []

result.append((1,0))
result.append((0,1))

def fibo(n):
    if len(result) < n+1:
        for i in range(len(result),n+1):
            a,b = result[i-1]
            c,d = result[i-2]
            result.append((a+c,b+d))
    return result[n]

for i in range(t):
    n = int(sys.stdin.readline())
    fibo(n)
    result_num.append(n)

for n in result_num:
    print(' '.join(list(map(str,result[n]))))