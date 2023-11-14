from collections import deque
import sys
import math

n = int(sys.stdin.readline())
ans = 0
for i in range(1,n+1):
    ans += i

print(ans)