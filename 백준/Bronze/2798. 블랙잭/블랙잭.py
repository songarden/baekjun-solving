import sys

n, m = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
answer = 0
for i in range(n-2):
    if numbers[i] >= m:
        continue
    for j in range(i+1,n-1):
        if numbers[j]+numbers[i] >= m:
            continue
        for k in range(j+1,n):
            if numbers[k]+numbers[j]+numbers[i] > m:
                continue
            answer = max(answer,numbers[k]+numbers[j]+numbers[i])

print(answer)