from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
maxNum = num_list[0]
minNum = num_list[0]

for num in num_list:
    maxNum = max(num,maxNum)
    minNum = min(num,minNum)

print(minNum , maxNum)