from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n , m  = map(int,sys.stdin.readline().split())
password = {}

for _ in range(n):
    site , pw = map(str,sys.stdin.readline().strip().split())
    password[site] = pw

answer = []

for _ in range(m):
    s = sys.stdin.readline().strip()
    answer.append(password[s])

for i in range(m):
    print(answer[i])