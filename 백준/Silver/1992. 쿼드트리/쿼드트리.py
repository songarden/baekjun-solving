import sys

n = int(sys.stdin.readline())
square = []

for i in range(n):
    square.append(list(map(int,sys.stdin.readline().strip())))

answer = []

# print(square)

def check_four_dimen(n,x,y):
    answer.append('(')
    division_square(n//2,x,y)
    division_square(n//2,x,y+n//2)
    division_square(n//2,x+n//2,y)
    division_square(n//2,x+n//2,y+n//2)
    answer.append(')')

def division_square(n,startX,startY):
    isSquare = True
    for i in range(startX,startX+n):
        for j in range(startY,startY+n):
            if not square[startX][startY] == square[i][j]:
                check_four_dimen(n,startX,startY)
                isSquare = False
                break
        if isSquare == False:
            break
    if isSquare == True:
        if square[startX][startY] == 0:
            answer.append(0)
        else: 
            answer.append(1)
def division_check(n):
    for i in range(n):
        for j in range(n):
            if not square[0][0] == square[i][j]:
                return 1
    return 0
check_four_dimen(n,0,0)
if division_check(n) == 0:
    print(square[0][0])
else:
    print(''.join(map(str,answer)))