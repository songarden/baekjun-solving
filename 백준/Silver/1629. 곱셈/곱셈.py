from collections import deque
import sys
import heapq

a,b,c = map(int,sys.stdin.readline().strip().split())

# while a <= c and b>=0:
#     a *= a
#     b -= 1
# result = a%c
# for i in range(b):
#     result = (result*a)%c

def div_mup(a,b):
    if b == 1:
        return a
    elif b%2 == 1:
        return div_mup(a, b//2)**2*a%c
    else:
        return div_mup(a, b//2)**2%c
result = div_mup(a,b)


print(result%c)