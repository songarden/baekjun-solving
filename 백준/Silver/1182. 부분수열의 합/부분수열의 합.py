import copy
import sys

##모든 부분집합의 합을 다 구한다음에 있는 개수 하나씩 카운트

n,s = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

nums = sorted(nums)
visited = [False for _ in range(n)]
count = 0
# print(nums, n, s)
def sum_of_sub(startIndex,m): #nums = 수열, m은 현재 값, s는 정답
    global n
    global s
    global count


    if m == s :
        count += 1
    
    for i in range(startIndex+1,n):
        if not visited[i]:
            visited[i] = True
            sum_of_sub(i,m+nums[i])
            visited[i] = False

for i in range(n):
    sum_of_sub(i,nums[i])

print(count)