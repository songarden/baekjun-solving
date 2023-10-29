from collections import deque
import heapq
import re
import sys
sys.setrecursionlimit(10**8)

testCase = int(sys.stdin.readline())
result = []
for i in range(testCase):
    Coins_num = int(sys.stdin.readline())

    Coins = list(map(int,sys.stdin.readline().split()))

    goal_coin = int(sys.stdin.readline())
    dp_list = [1]+[0 for _ in range(goal_coin)]
    for i in range(len(Coins)):
        This_Coin = Coins[i]
        for j in range(This_Coin,goal_coin+1):
            dp_list[j] += dp_list[j-This_Coin]
    result.append(dp_list[goal_coin])

for answer in result:
    print(answer)