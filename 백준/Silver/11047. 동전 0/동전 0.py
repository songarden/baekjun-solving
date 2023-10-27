from collections import deque
import heapq
import re
import sys

n, cost = map(int,sys.stdin.readline().strip().split())
coinList = []

for i in range(n):
    coin = int(sys.stdin.readline())
    if coin <= cost:
        coinList.append(coin)


coinList.sort()
count = 0

def sol(cost):
    global count
    while coinList:
        thisCoin = coinList.pop()
        if cost % thisCoin == 0:
            return count+(cost//thisCoin)
        else:
            count += cost // thisCoin
            cost = cost % thisCoin
                


print(sol(cost))