import sys

n = int(sys.stdin.readline())

rgb_house = []

for i in range(n) :
    rgb_house.append(list(map(int,sys.stdin.readline().split())))
    
dp = []

dp.append(rgb_house[0])

for i in range(1,n) :
    temp = []
    for j in range(3) :
        temp.append(rgb_house[i][j] + min(dp[i-1][(j+1)%3] , dp[i-1][(j+2)%3]))
    
    dp.append(temp)

print(min(dp[n-1]))