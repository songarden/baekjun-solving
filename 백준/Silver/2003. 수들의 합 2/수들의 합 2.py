import sys

n,m = map(int,sys.stdin.readline().split())

queue = list(map(int,sys.stdin.readline().split()))
ans = 0
if queue[-1] == m:
    ans += 1
i = 0
j = 0
sum = queue[i]
while(i<n-1):
    if sum < m:
        if j >= n-1:
            break
        j += 1
        sum += queue[j]
    elif sum == m:
        ans += 1
        if j >= n-1:
            break
        sum -= queue[i]
        i += 1
        j += 1
        sum += queue[j]
    else :
        if i == j:
            i += 1
            j += 1
            sum = queue[i]
        else:
            sum -= queue[i]
            i += 1

print(ans)
        


