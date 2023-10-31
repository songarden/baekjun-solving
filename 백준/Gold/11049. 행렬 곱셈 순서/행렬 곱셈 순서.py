import sys

n = int(sys.stdin.readline())
INF = float('inf')

matrix_p = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    if not matrix_p:
        matrix_p.append(a)
    matrix_p.append(b)

cal_count = [[0 for _ in range(n+1)] for _ in range(n+1)]

for l in range(2,n+1):
    for i in range(1,n-l+2):
        j = i+l-1
        cal_count[i][j] = INF
        for k in range(i,j):
            cal_count[i][j] = min(cal_count[i][j] , cal_count[i][k] + cal_count[k+1][j] + (matrix_p[i-1]*matrix_p[k]*matrix_p[j]))

print(cal_count[1][n])