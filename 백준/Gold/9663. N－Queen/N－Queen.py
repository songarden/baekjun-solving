import sys
import math

count = 0
n = int(sys.stdin.readline())
pos = []

line_A = [False]*n
line_B = [False]*(2*n-1)
line_C = [False]*(2*n-1)

def setting(i,n) :
    global count

    for j in range(n):
        if(not line_A[j]
           and not line_B[i+j]
           and not line_C[i-j+n-1]):
            
            if i==(n-1) :
                count = count+1
            else:
                line_A[j] = line_B[i+j] = line_C[i-j+n-1] = True
                setting(i+1,n)
                line_A[j] = line_B[i+j] = line_C[i-j+n-1] = False

setting(0,n)
print(count)

## 2차 배열로 구현하는 것도 한번 생각해보기

# def chessTableReset(n) :
#     tempTable = [0]*n
#     chessTable = []
#     for i in range(n):
#         chessTable.append(tempTable)
#     return chessTable

# for i in range(row,n):
#     for j in range(n):
#         if table[i][j] == 0 :
#             table[i][j] = 1
#             table[j][j] = 1
#             set
#     for j in range(n):
#         if table[i-1][j] == 0:
#             table[i][j] = 1
#             continue
#         else :

## 생각해보니 대각선 검사 때 위 방법이 시간 복잡도가 낮아서 위가 최선임