from collections import deque
import sys
import heapq

n = int(sys.stdin.readline())
square = []
one_num = 0
zero_num = 0
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    square.append(line)


def division_square(n,startX,startY):
    global zero_num
    global one_num
    isSquare = True
    for i in range(startX,startX+n):
        for j in range(startY,startY+n):
            if not square[startX][startY] == square[i][j]:
                isSquare = False
                division_square(n//2,startX,startY)
                division_square(n//2,startX,startY+n//2)
                division_square(n//2,startX+n//2,startY)
                division_square(n//2,startX+n//2,startY+n//2)
                break
        if isSquare == False:
            break
    if isSquare == True:
        if square[startX][startY] == 0:
            zero_num +=1
        else:
            one_num +=1

division_square(n,0,0)
print(zero_num)
print(one_num)