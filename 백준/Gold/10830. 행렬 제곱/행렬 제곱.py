from collections import deque
import sys
import heapq

n,b = map(int,sys.stdin.readline().strip().split())

matrix = []
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    matrix.append(temp)

def matrix_solve(matrixA, matrixB):
    global n
    result = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrixA[i][k]*matrixB[k][j]
            result[i][j] = result[i][j]%1000

    return result

def problem_solve(b):
    global n
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j]%1000
        return matrix
    elif b%2 == 0:
        half = problem_solve(b//2)
        return matrix_solve(half,half)
    else:
        half = problem_solve(b//2)
        temp = matrix_solve(half,half)
        return matrix_solve(temp,matrix)



list = problem_solve(b)
for i in range(n):
    print(' '.join(map(str,list[i])))