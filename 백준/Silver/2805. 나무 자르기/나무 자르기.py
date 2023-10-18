from collections import deque
import sys
import heapq

n, m= map(int,sys.stdin.readline().strip().split())

trees = list(map(int, sys.stdin.readline().strip().split()))
# print(trees)

trees = sorted(trees,reverse=True)

def search_binary(m):
    global n
    pl = 0
    pr = trees[0]
    while True :
        temp = 0
        pc = (pl+pr)//2
        for i in range(n):
            adding = trees[i]-pc
            if adding <= 0:
                break
            temp += adding
        if temp == m:
            return pc
        elif temp>m:
            pl = pc+1
            if pl > pr:
                return pc
        else:
            pr = pc -1
            if pl > pr:
                return pc-1

print(search_binary(m))