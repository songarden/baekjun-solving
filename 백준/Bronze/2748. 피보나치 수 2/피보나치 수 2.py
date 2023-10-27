from collections import deque
import heapq
import re
import sys

n = int(sys.stdin.readline())
fibo_result = [0,1] + [-1 for _ in range(n-1)]

def fibo(n):
    if fibo_result[n] >= 0:
        return fibo_result[n]
    else:
        fibo_result[n] = fibo(n-1) + fibo(n-2)
        return fibo_result[n]

print(fibo(n))