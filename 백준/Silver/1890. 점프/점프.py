import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
jump_map = []
for _ in range(n):
    jump_map.append(list(map(int,sys.stdin.readline().split())))

visited_count = [[0 for _ in range(n)] for _ in range(n)]

def sol(i,j):
    global n
    this_function_visit_count = 0
    jump_count = jump_map[i][j]

    if i == n-1 and j == n-1:
        return 1
    
    if jump_count == 0:
        return 0
    
    if visited_count[i][j] != 0:
        return visited_count[i][j]
    

    if i+jump_count < n:
        this_function_visit_count += sol(i+jump_count,j)
    if j+jump_count < n:
        this_function_visit_count += sol(i,j+jump_count)
    
    visited_count[i][j] = this_function_visit_count
    return visited_count[i][j]

print(sol(0,0))