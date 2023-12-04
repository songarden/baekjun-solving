import sys


n=int(sys.stdin.readline())

game_map = []
for _ in range(n):
    game_map.append(list(map(str,sys.stdin.readline().strip())))

ans = 0

if n <=2 :
    print(0)
    sys.exit()

if game_map[0][0] == '1':
    game_map[1][1] = '*'
    ans += 1
    if n == 3:
        print(ans)
        sys.exit()
if game_map[0][n-1] == '1':
    game_map[1][n-2] = '*'
    ans += 1
if game_map[n-1][0] == '1':
    game_map[n-2][1] = '*'
    ans += 1
if game_map[n-1][n-1] == '1':
    game_map[n-2][n-2] = '*'
    ans += 1

if n <=4 :
    print(ans)
    sys.exit()

for i in range(1,n-2):
    temp = 0
    for j in range(i-1,i+1):
        if game_map[1][j] == '*':
            temp += 1
    if temp != int(game_map[0][i]):
        if game_map[1][i+1] == '*':
            continue
        game_map[1][i+1] = '*'
        ans += 1
    
    temp = 0
    for j in range(i-1,i+1):
        if game_map[j][n-2] == '*':
            temp += 1
    if temp != int(game_map[i][n-1]):
        if game_map[i+1][n-2] == '*':
            continue
        game_map[i+1][n-2] = '*'
        ans += 1
    
    temp = 0
    for j in range(i-1,i+1):
        if game_map[n-2][j] == '*':
            temp += 1
    if temp != int(game_map[n-1][i]):
        if game_map[n-2][i+1] == '*':
            continue
        game_map[n-2][i+1] = '*'
        ans += 1
        
    temp = 0
    for j in range(i-1,i+1):
        if game_map[j][1] == '*':
            temp += 1
    if temp != int(game_map[i][0]):
        if game_map[i+1][1] == '*':
            continue
        game_map[i+1][1] = '*'
        ans += 1

ans += (n-4)**2

print(ans)