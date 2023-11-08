from collections import deque,defaultdict
import heapq
import re
import sys
import math
sys.setrecursionlimit(10**8)

n , endI, endJ = map(int,sys.stdin.readline().split())
count = 0



def div_dfs(i,j,dim):
    global count , endI, endJ
    if dim == 1:
        for dx, dy in (0,0),(0,1),(1,0),(1,1):
            if endI == dx+i and endJ == dy+j:
                print(count)
                return
            count += 1
    else:
        if i+2**(dim-1)>endI>=i and j+2**(dim-1)>endJ>=j:
            div_dfs(i,j,dim-1)
        elif i+2**(dim-1)>endI>=i and endJ >= j+2**(dim-1):
            count += ((2**(dim-1))**2)*1
            div_dfs(i,j+2**(dim-1),dim-1)
        elif endI >= i+2**(dim-1) and j+2**(dim-1)>endJ>=j:
            count += ((2**(dim-1))**2)*2
            div_dfs(i+2**(dim-1),j,dim-1)
        elif endI >= i+2**(dim-1) and endJ >= j+2**(dim-1):
            count += ((2**(dim-1))**2)*3
            div_dfs(i+2**(dim-1),j+2**(dim-1),dim-1)

div_dfs(0,0,n)