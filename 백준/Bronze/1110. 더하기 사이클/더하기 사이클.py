from collections import deque
import copy
import sys
import heapq

n = int(sys.stdin.readline())

def solve(n):
    count = 0
    first = n
    while True:
        count += 1
        right = (n%10)
        left = (n//10 + n%10)%10
        n = right*10 + left
        if first == n:
            return count

print(solve(n))