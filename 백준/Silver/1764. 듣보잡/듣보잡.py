import sys

n,m = map(int,sys.stdin.readline().split())

checkDict = {}
answer = []

for _ in range(n):
    fstItem = sys.stdin.readline().strip()
    checkDict[fstItem] = 1

for _ in range(m):
    checkItem = sys.stdin.readline().strip()
    if checkItem in checkDict:
        answer.append(checkItem)

list.sort(answer)
print(len(answer))

for ans in answer:
    print(ans)