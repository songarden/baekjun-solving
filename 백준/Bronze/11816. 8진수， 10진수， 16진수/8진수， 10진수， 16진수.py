import sys
import math

n = sys.stdin.readline().strip()

if n[0] == '0':
    if n[1] == 'x':
        newNum = n[2:]
        num = int(newNum,16)
        print(num)
    else:
        newNum = n[1:]
        num = int(newNum,8)
        print(num)
else:
    print(n)